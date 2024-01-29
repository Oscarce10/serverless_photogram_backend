import os
from typing import Optional

from fastapi import APIRouter, Query
from sentry_sdk import capture_exception
from starlette.responses import JSONResponse

from app.api.v1.serializers import ResponseSerializer, SortSerializer, \
    LikeDislikePhotoSerializer
from app.core.handlers import CategoriesHandler
from app.core.utils import send_slack_notification

"""
-------------------------  Categories -------------------------
"""
categories = APIRouter()


@categories.get(
    "/",
    tags=["Get all categories"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def get_categories_view():
    """ **Get Categories**

    Pending

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.get_categories()
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        capture_exception(e)
        return JSONResponse(
            content={
                "status": 500,
                "message": "internal server error"
            }, status_code=500
        )


@categories.get(
    "/{category_id}/",
    tags=["Get a category by id"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def get_category_view(
        category_id: int
):
    """ **Get Categories**

    Pending

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.get_category(
            category_id=category_id
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        capture_exception(e)
        return JSONResponse(
            content={
                "status": 500,
                "message": "internal server error"
            }, status_code=500
        )


"""
-------------------------  ----------------- -------------------------
"""

"""
-------------------------  photos -------------------------
"""
photos = APIRouter()


@photos.get(
    "/",
    tags=["Get all photos"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def get_photos_view(
        category_id: Optional[int] = Query(None),
        current_page: int = 1,
        items_per_page: int = 10,
        order_by: SortSerializer = "desc"
):
    """ **Get Photos**

    Pending

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.get_photos(
            category_id=category_id,
            current_page=current_page,
            items_per_page=items_per_page,
            order_by=order_by
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        capture_exception(e)
        send_slack_notification(
            username="Photogram API",
            icon_emoji=":robot_face:",
            message=str(e),
        )
        return JSONResponse(
            content={
                "status": 500,
                "message": "internal server error, exception caught, "
                           "sentry: {}".format(os.getenv("SENTRY_DSN"))
            }, status_code=500
        )


@photos.put(
    "/",
    tags=["Like a photo"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def set_like_dislike_view(
        photo: LikeDislikePhotoSerializer
):
    """ **Like a photo**

    Increments the likes of a photo by 1

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.like_dislike_photo(
            photo_id=photo.photo_id,
            action=photo.action
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        capture_exception(e)
        return JSONResponse(
            content={
                "status": 500,
                "message": "Internal Server Error"
            }, status_code=500
        )


@photos.get(
    "/{photo_id}/",
    tags=["Get photo information"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def get_photo_view(
        photo_id: int
):
    """ **Like a photo**

    Increments the likes of a photo by 1

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.get_photo(
            photo_id=photo_id
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        capture_exception(e)
        return JSONResponse(
            content={
                "status": 500,
                "message": "Internal Server Error"
            }, status_code=500
        )
