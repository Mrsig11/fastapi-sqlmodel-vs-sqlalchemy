import pytest
from app.schemas.todo import TodoCreate
from app.core.database import get_db
from app.repositories.factory import get_todo_repository


@pytest.mark.benchmark
def test_repository_create_benchmark(benchmark):
    gen = get_db()
    db = next(gen)

    repo = get_todo_repository(db)

    def create():
        repo.create(TodoCreate(title="Benchmark Todo"))

    benchmark(create)
