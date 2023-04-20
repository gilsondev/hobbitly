from src.services.urls import URLService
from src.schemas.urls import URLBase
from src.core.config import settings


def test_short_url(db_session, mocker):
    service = URLService(db_session)
    url_schema = URLBase(target_url="http://google.com.br")

    mocker.patch.object(service, "_create_short_id", return_value="1q2w3e4r")
    result = service.short_url(url_schema)

    service._create_short_id.assert_called_once()
    assert result == {
        "target_url": url_schema.target_url,
        "is_active": True,
        "clicks": 0,
        "url": f"{settings.SITE_URL}/1q2w3e4r",
    }


def test_create_short_id(db_session):
    service = URLService(db_session)
    short_id = service._create_short_id()

    assert short_id is not None
