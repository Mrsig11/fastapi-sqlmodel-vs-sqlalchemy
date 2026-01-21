import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 50,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% < 500ms
    http_req_failed: ['rate<0.01'],   // < 1% d'erreurs
  },
};

const BASE_URL = 'http://localhost:8000';

export default function () {
  // Health check
  let res = http.get(`${BASE_URL}/health`);
  check(res, {
    'health status 200': (r) => r.status === 200,
  });

  // Create todo
  res = http.post(
    `${BASE_URL}/todos`,
    JSON.stringify({
      title: 'k6 todo',
      description: 'created by k6',
    }),
    { headers: { 'Content-Type': 'application/json' } }
  );

  check(res, {
    'todo created': (r) => r.status === 201 || r.status === 200,
  });

  sleep(1);
}
