from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.todo import TodoCreate, TodoRead
from app.services.todo_service import TodoService
from app.core.dependencies import get_todo_service

router = APIRouter(tags=["Todos"])


@router.get("/", response_model=List[TodoRead])
def list_todos(
    service: TodoService = Depends(get_todo_service),
):
    return service.list_todos()


@router.post(
    "/", response_model=TodoRead, status_code=status.HTTP_201_CREATED
)
def create_todo(
    payload: TodoCreate,
    service: TodoService = Depends(get_todo_service),
):
    return service.create_todo(payload)

@router.get("/{id}", response_model=TodoRead)
def get_todo(
    id: int,
    service: TodoService = Depends(get_todo_service),
):
    return service.get_todo(id)

@router.put("/{id}", response_model=TodoRead)
def update_todo(
    id: int,
    payload: TodoCreate,
    service: TodoService = Depends(get_todo_service),
):
    return service.update_todo(id, payload)

@router.delete("/{id}", response_model=TodoRead)
def delete_todo(
    id: int,
    service: TodoService = Depends(get_todo_service),
):
    return service.delete_todo(id)
