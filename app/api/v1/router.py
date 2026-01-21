from fastapi import APIRouter
from app.api.v1.endpoints import todos, health

api_router = APIRouter()

# Endpoints métier
api_router.include_router(
    todos.router,
    prefix="/todos",
)

# Endpoints techniques
api_router.include_router(
    health.router,
)
