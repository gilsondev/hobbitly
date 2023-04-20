from pydantic import BaseModel, AnyHttpUrl


class URLBase(BaseModel):
    target_url: AnyHttpUrl


class URLResponse(URLBase):
    is_active: bool
    clicks: int
    url: AnyHttpUrl
