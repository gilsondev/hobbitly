from src import __version__
from src.core.config import settings
from src.services.urls import URLService


def test_root_endpoint(client):
    resp = client.get("/")

    assert resp.status_code == 200
    assert resp.json() == {"app": settings.TITLE, "version": __version__}


def test_short_url(client, mocker):
    short_id = "1q2w3e4r"
    payload = {"target_url": "http://google.com"}
    mocker.patch.object(URLService, "_create_short_id", return_value=short_id)

    resp = client.post("/short/", json=payload)

    assert resp.status_code == 201
    assert resp.json() == {
        "target_url": "http://google.com",
        "is_active": True,
        "clicks": 0,
        "url": f"{settings.SITE_URL}/{short_id}",
    }
