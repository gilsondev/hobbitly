import string
import random

from sqlmodel import Session
from src.schemas.urls import URLBase, URLResponse
from src.core.config import settings
from src.models import ShortenedURL


class URLService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def _create_short_id(self) -> str:
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(settings.SHORT_ID_SIZE))

    def short_url(self, url: URLBase) -> URLResponse:
        short_id = self._create_short_id()
        shortened_url = ShortenedURL(target_url=url.target_url, short_url=short_id)
        self.session.add(shortened_url)
        self.session.commit()
        self.session.refresh(shortened_url)
        return URLResponse(
            target_url=shortened_url.target_url,
            is_active=shortened_url.is_active,
            clicks=shortened_url.clicks,
            url=f"{settings.SITE_URL}/{short_id}",
        )
