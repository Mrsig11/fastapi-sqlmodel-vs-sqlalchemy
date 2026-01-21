from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.router import api_router
from app.core.database import init_db
from app.core.logging import setup_logging

# setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # shutdown logic (optionnel)


app = FastAPI(
    title="Todo API – SQLModel vs SQLAlchemy Benchmark",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api/v1")
