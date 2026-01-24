from sqlalchemy.orm import Session
from app.models.sqlalchemy.todo import Todo
from app.schemas.todo import TodoCreate, TodoRead

class SqlAlchemyTodoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Todo).all()

    def create(self, data: TodoCreate):
        todo = Todo(**data.model_dump())
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    
    def update(self, id: int, data: TodoRead):
        todo = self.session.query(Todo).filter(Todo.id == id).first()
        todo.title = data.title
        todo.completed = data.completed
        self.session.commit()
        self.session.refresh(todo)
        return todo
    
    def delete(self, id: int):
        todo = self.session.query(Todo).filter(Todo.id == id).first()
        self.session.delete(todo)
        self.session.commit()
        return todo
    
    def get(self, id: int):
        return self.session.query(Todo).filter(Todo.id == id).first()
