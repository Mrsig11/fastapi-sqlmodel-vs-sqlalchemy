from sqlalchemy import Column, Integer, String, Boolean
from app.models.sqlalchemy.base import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"Todo(id={self.id}, title={self.title}, completed={self.completed})"