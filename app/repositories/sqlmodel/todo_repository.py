from sqlmodel import Session, select
from app.models.sqlmodel.todo import Todo
from app.schemas.todo import TodoCreate, TodoRead

class SqlModelTodoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Todo)
        results = self.session.exec(statement).all()
        return results

    def create(self, data: TodoCreate):
        todo = Todo(**data.model_dump())
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    
    def update(self, id: int, data: TodoCreate):
        todo = self.session.get(Todo, id)
        todo.title = data.title
        todo.completed = data.completed
        self.session.commit()
        self.session.refresh(todo)
        return todo
    
    def delete(self, id: int):
        todo = self.session.get(Todo, id)
        self.session.delete(todo)
        self.session.commit()
        return todo
    
    def get(self, id: int):
        todo = self.session.get(Todo, id)
        return todo
