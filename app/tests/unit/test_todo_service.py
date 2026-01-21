from app.schemas.todo import TodoCreate
from app.services.todo_service import TodoService
from app.core.database import get_db
from app.repositories.factory import get_todo_repository


def test_service_create_and_list():
    gen = get_db()
    db = next(gen)

    repo = get_todo_repository(db)
    service = TodoService(repo)

    service.create_todo(TodoCreate(title="Service Todo"))

    todos = service.list_todos()
    assert any(t.title == "Service Todo" for t in todos)
