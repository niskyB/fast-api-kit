from fastapi import APIRouter, FastAPI

from app.core.config import settings


def include_router(app: FastAPI) -> None:
    api_router = APIRouter()

    app.include_router(api_router, prefix=settings.API_V1_STR)
