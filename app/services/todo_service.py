from app.repositories.interfaces.todo_repository import TodoRepository

class TodoService:
    def __init__(self, repo: TodoRepository):
        self.repo = repo

    def list_todos(self):
        return self.repo.get_all()

    def create_todo(self, data):
        return self.repo.create(data)
    
    def update_todo(self, id, data):
        return self.repo.update(id, data)
    
    def delete_todo(self, id):
        return self.repo.delete(id)
    
    def get_todo(self, id):
        return self.repo.get(id)
