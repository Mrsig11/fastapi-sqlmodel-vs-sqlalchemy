import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_db, init_db


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    os.environ["ORM_ENGINE"] = os.getenv("ORM_ENGINE", "sqlmodel")
    init_db()
    yield


@pytest.fixture()
def client():
    return TestClient(app)
