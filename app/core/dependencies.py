from fastapi import Depends
from app.core.database import get_db
from app.repositories.factory import get_todo_repository
from app.services.todo_service import TodoService


def get_todo_service(db=Depends(get_db)) -> TodoService:
    repo = get_todo_repository(db)
    return TodoService(repo)
