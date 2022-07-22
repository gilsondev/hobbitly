import pytest
import warnings
import alembic

from fastapi.testclient import TestClient
from alembic.config import Config
from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlmodel import create_engine

from hobbitly.app import app
from hobbitly.config import settings


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    config = Config("alembic.ini")

    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


@pytest.fixture(scope="session")
def db_connection():
    engine = create_engine(f"{settings.database_url}_test")
    return engine.connect()


@pytest.fixture(scope="session")
def db_session(db_connection: Connection):
    transaction = db_connection.begin()

    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=db_connection)
    )
    transaction.rollback()
