from collections.abc import Generator
from fastapi import Depends
from sqlmodel import Session as SQLSession, create_engine

from src.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
)


def get_session() -> Generator:
    with SQLSession(engine) as session:
        yield session


Session = Depends(get_session)
