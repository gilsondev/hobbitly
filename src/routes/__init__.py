from typing import Dict

from fastapi import APIRouter

from src import __version__
from src.core.config import settings
from src.routes.urls import router as urls_router

main_router = APIRouter()


@main_router.get("/", summary="Return metadata of application")
def index() -> Dict:
    return {"app": settings.TITLE, "version": __version__}


__all__ = [main_router, urls_router]
