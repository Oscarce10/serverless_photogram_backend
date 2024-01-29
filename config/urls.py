from fastapi import APIRouter

from app.api.v1.urls import api
from app.meta import views as meta

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    api,
    prefix="/api/v1"
)
