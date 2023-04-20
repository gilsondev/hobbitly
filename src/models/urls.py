from typing import Optional

from sqlmodel import SQLModel, Field


class ShortenedURL(SQLModel, table=True):
    __tablename__ = "shortened_urls"

    id: Optional[int] = Field(default=None, primary_key=True)
    target_url: str
    is_active: bool = True
    clicks: int = 0
    short_url: str
