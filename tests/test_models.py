from src.models.urls import ShortenedURL


def test_shortened_url_model():
    target_url = "http://google.com"
    shortened_url = ShortenedURL(target_url=target_url, short_url="1q2w3e")

    assert shortened_url is not None
    assert shortened_url.target_url == target_url
    assert shortened_url.is_active
    assert shortened_url.clicks == 0
    assert shortened_url.short_url == "1q2w3e"


def test_new_shortened_url(db_session):
    target_url = "http://google.com"
    shortened_url = ShortenedURL(target_url=target_url, short_url="1q2w3e")

    db_session.add(shortened_url)
    db_session.commit()
    db_session.refresh(shortened_url)

    assert shortened_url.id == 1
