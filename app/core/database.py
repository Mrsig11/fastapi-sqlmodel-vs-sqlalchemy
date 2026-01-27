from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import ORM_ENGINE

from app.models.sqlalchemy.base import Base as SA_Base
from app.models.sqlmodel.todo import Todo as SQLModelTodo

print(ORM_ENGINE)

DATABASE_URL = "sqlite:///./todo.db"

# --- SQLModel ---
sqlmodel_engine = create_engine(
    DATABASE_URL,
    echo=False,
)

# --- SQLAlchemy ---
sqlalchemy_engine = sa_create_engine(
    DATABASE_URL,
    echo=False,
)

SqlAlchemySessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sqlalchemy_engine,
)


def get_db():
    """
    Fournit une session DB en fonction de l'ORM sélectionné
    """
    if ORM_ENGINE == "sqlalchemy":
        db = SqlAlchemySessionLocal()
        try:
            yield db
        finally:
            db.close()
    elif ORM_ENGINE == "sqlmodel":
        with Session(sqlmodel_engine) as session:
            yield session


def init_db():
    if ORM_ENGINE == "sqlalchemy":
        SA_Base.metadata.create_all(bind=sqlalchemy_engine)
    elif ORM_ENGINE == "sqlmodel":
        SQLModel.metadata.create_all(sqlmodel_engine)
