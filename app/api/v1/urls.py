from fastapi import APIRouter

from app.api.v1.views import categories, photos

api = APIRouter()

api.include_router(
    categories,
    prefix="/categories"
)

api.include_router(
    photos,
    prefix="/photos"
)
