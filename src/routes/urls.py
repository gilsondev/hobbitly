from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from src.core.config import settings
from src.schemas.urls import URLBase, URLResponse
from src.core.database import get_session
from src.services.urls import URLService

router = APIRouter(prefix="/short")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=URLResponse)
def short_url(url_data: URLBase, session: Session = Depends(get_session)) -> dict:
    service = URLService(session)
    return service.short_url(url_data)
