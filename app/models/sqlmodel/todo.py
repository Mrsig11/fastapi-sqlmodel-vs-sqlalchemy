from typing import Optional
from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    __tablename__ = "todos"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    completed: bool = False
    
    def __repr__(self):
        return f"Todo(id={self.id}, title={self.title}, completed={self.completed})"
