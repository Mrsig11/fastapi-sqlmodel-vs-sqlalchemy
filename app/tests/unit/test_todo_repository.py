from app.schemas.todo import TodoCreate
from app.core.database import get_db
from app.repositories.factory import get_todo_repository


def test_create_and_list_todos():
    gen = get_db()
    db = next(gen)

    repo = get_todo_repository(db)

    todo = repo.create(TodoCreate(title="Test Todo"))
    todos = repo.get_all()

    assert todo.id is not None
    assert len(todos) >= 1
