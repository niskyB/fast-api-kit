from fastapi import APIRouter, FastAPI

from app.core.config import settings
from app.api.api_v1.endpoints import user


def include_router(app: FastAPI) -> None:
    api_router = APIRouter()
    api_router.include_router(user.router, prefix="/user", tags=["User"])

    app.include_router(api_router, prefix=settings.API_V1_STR)
