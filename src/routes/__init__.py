from typing import Dict

from fastapi import APIRouter

from src import __version__
from src.core.config import settings

main_router = APIRouter()


@main_router.get("/", summary="Return metadata of application")
def index() -> Dict:
    return {"app": settings.TITLE, "version": __version__}
