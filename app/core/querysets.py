import math
import os

from pymongo import MongoClient


class Queryset:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI') or
                                  'mongodb://localhost:27017/photogram')

    def get_all_categories(self):
        db = self.client.photogram
        collection = db.categories
        return list(collection.find({}, {"_id": 0}))

    def get_category(self, category_id: int):
        db = self.client.photogram
        collection = db.categories
        category = collection.find_one({"id": category_id})
        if category:
            return {
                "status": 200,
                "data": category
            }
        return {
            "status": 404,
            "data": {
                "message": "Category not found"
            }
        }

    def get_all_photos(
            self,
            category_id: int,
            current_page: int,
            items_per_page: int,
            order_by: str,
    ):
        db = self.client.photogram
        collection = db.photos
        qy = {
            "categoryId": category_id
        } if category_id is not None else {}
        count = collection.count_documents(qy)
        photos = list(
            collection.find(
                qy,
                {
                    "_id": 0
                }
            ).skip(
                (current_page - 1) * items_per_page
            ).limit(
                items_per_page
            ).sort(
                order_by
            )
        )
        return {
            "status": 200,
            "data": photos,
            "meta": {
                "current_page": current_page,
                "items_per_page": items_per_page,
                "total_items": count,
                "total_pages": math.ceil(count / items_per_page)
            }
        }

    def get_photo(
            self,
            photo_id: int,
    ):
        db = self.client.photogram
        collection = db.photos
        photo = collection.find_one(
            {
                "id": photo_id
            },
            {
                "_id": 0
            }
        )
        return {
            "status": 200,
            "data": photo,
        }

    def like_dislike_photo(self, photo_id: int, action: str):
        db = self.client.photogram
        collection = db.photos
        photo = collection.find_one({"id": photo_id})
        if photo:
            collection.update_one(
                {"id": photo_id},
                {
                    "$set": {
                        "likes": photo["likes"] + 1 if action == "like" else
                        photo["likes"] - 1
                    }
                }
            )
            return {
                "status": 200,
                "data": {
                    "message": "Photo liked successfully" if action == "like"
                    else "Photo disliked successfully"
                }
            }
        return {
            "status": 409,
            "data": {
                "message": "Photo not found"
            }
        }
