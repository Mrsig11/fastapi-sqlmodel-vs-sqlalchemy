from typing import Protocol, List
from app.schemas.todo import TodoCreate, TodoRead

class TodoRepository(Protocol):
    def get_all(self) -> List[TodoRead]:
        ...

    def create(self, data: TodoCreate) -> TodoRead:
        ...

    def update(self, id: int, data: TodoCreate) -> TodoRead:
        ...

    def delete(self, id: int) -> TodoRead:
        ...

    def get(self, id: int) -> TodoRead:
        ...