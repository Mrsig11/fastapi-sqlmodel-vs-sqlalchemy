import os
from app.core.database import get_db
from app.schemas.todo import TodoCreate
from app.repositories.factory import get_todo_repository

os.environ.setdefault("ORM_ENGINE", "sqlmodel")


def seed(count: int = 1000):
    gen = get_db()
    db = next(gen)

    repo = get_todo_repository(db)

    for i in range(count):
        repo.create(TodoCreate(title=f"Todo #{i+1}"))

    print(f"✅ Seeded {count} todos")


if __name__ == "__main__":
    seed(1000)
