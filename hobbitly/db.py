from venv import create
from fastapi import Depends
from sqlmodel import Session, create_engine

from hobbitly.config import settings


engine = create_engine(
    settings.database_url,
    echo=settings.db_echo
)


def get_session():
    with Session(engine) as session:
        yield session


ActiveSession = Depends(get_session)
