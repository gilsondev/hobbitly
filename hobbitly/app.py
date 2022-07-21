from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from hobbitly.config import settings

VERSION = "0.1.0"
DESCRIPTION = """
Um simples, mas honesto encurtador de URLs
"""


app = FastAPI(
    title="Hobbitly",
    description=DESCRIPTION,
    version=VERSION,
    contact={
        "name": "Gilson Filho",
        "url": "https://github.com/gilsondev/hobbitly",
        "email": "me@gilsondev.in",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=settings.cors_allow_credentials,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
    )


@app.on_event("startup")
def on_startup():
    pass
