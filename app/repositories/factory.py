from app.core.config import ORM_ENGINE

def get_todo_repository(db_session):
    if ORM_ENGINE == "sqlalchemy":
        from app.repositories.sqlalchemy.todo_repository import (
            SqlAlchemyTodoRepository
        )
        return SqlAlchemyTodoRepository(db_session)

    from app.repositories.sqlmodel.todo_repository import (
        SqlModelTodoRepository
    )
    return SqlModelTodoRepository(db_session)
