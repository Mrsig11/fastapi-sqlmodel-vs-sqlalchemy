import pytest


@pytest.mark.benchmark
def test_api_list_todos_benchmark(benchmark, client):
    benchmark(lambda: client.get("/api/v1/todos/"))
