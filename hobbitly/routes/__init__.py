from fastapi import APIRouter
import hobbitly

api_router = APIRouter()


@api_router.get("/")
def index():
    return {"version": hobbitly.__version__}
