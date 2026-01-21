from locust import HttpUser, task, between

class TodoUser(HttpUser):
    """
    Simule un utilisateur de l'API Todos
    """
    wait_time = between(1, 3)

    @task(3)
    def health_check(self):
        self.client.get("/api/v1/health/")

    @task(5)
    def list_todos(self):
        self.client.get("/api/v1/todos/")

    @task(2)
    def create_todo(self):
        self.client.post(
            "/api/v1/todos/",
            json={
                "title": "Load test",
                "description": "Created by Locust"
            }
        )
