import os

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine

from src import models
from src.app import app
from src.core.config import settings
from src.core.database import get_session

os.environ["DATABASE_URL"] = "postgres://postgres:postgres@localhost:5435/hobbitly_test"


@pytest.fixture(scope="session")
def engine():
    return create_engine(settings.DATABASE_URL)


@pytest.fixture(scope="session")
def database(engine):
    models.SQLModel.metadata.create_all(engine)
    yield engine
    models.SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(database):
    session = Session(database)
    yield session
    session.close()


@pytest.fixture(scope="function")
def client(db_session):
    def _get_session_override():
        return db_session

    app.dependency_overrides[get_session] = _get_session_override
    with TestClient(app) as test_client:
        yield test_client
