from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import hobbitly
from hobbitly.config import settings
from hobbitly.routes import api_router


app = FastAPI(
    title=hobbitly.__project__,
    description=hobbitly.__description__,
    version=hobbitly.__version__,
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


app.include_router(api_router)


@app.on_event("startup")
def on_startup():
    pass
