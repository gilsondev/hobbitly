from typing import List
from pydantic import BaseSettings
from decouple import config, Csv

from pathlib import Path

ROOT = Path(__file__)


class Settings(BaseSettings):
    debug: bool = config("DEBUG", default=False, cast=bool)
    secret_key: str = config("SECRET_KEY")
    host: str = config("HOST", default="127.0.0.1")
    port: str = config("PORT", default="8000")
    log_level: str = config("LOG_LEVEL", default="info")
    reload: bool = config("RELOAD", default=False, cast=bool)
    database_url: str = config("DATABASE_URL", default="sqlite://")
    db_echo: bool = True if config("DEBUG") else False
    cors_origins: List[str] = config("CORS_ORIGIN", cast=Csv())
    cors_allow_credentials: bool = config(
        "CORS_ALLOW_CREDENTIALS", default=False, cast=bool
    )
    cors_allow_methods: List[str] = config("CORS_ALLOW_METHODS", cast=Csv())
    cors_allow_headers: List[str] = config("CORS_ALLOW_HEADERS", cast=Csv())


settings = Settings()
