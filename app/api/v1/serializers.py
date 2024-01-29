from enum import Enum
from typing import Union, Optional

from pydantic import BaseModel


class ResponseSerializer(BaseModel):
    status: int
    message: Optional[str]
    data: Union[dict, list]


class SortSerializer(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


class LikeDislike(str, Enum):
    LIKE = 'like'
    DISLIKE = 'dislike'


class LikeDislikePhotoSerializer(BaseModel):
    photo_id: int
    action: LikeDislike
