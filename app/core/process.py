from app.core.querysets import Queryset


class CategoriesProcess:
    @staticmethod
    def get_categories():
        qs = Queryset()
        res = qs.get_all_categories()
        return {
            "status": 200,
            "data": res
        }

    @staticmethod
    def get_category(category_id: int):
        qs = Queryset()
        res = qs.get_category(category_id)
        return {
            "status": 200,
            "data": res
        }


class PhotosProcess:
    @staticmethod
    def get_photos(
            category_id: int,
            current_page: int,
            items_per_page: int,
            order_by: str
    ):
        qs = Queryset()
        return qs.get_all_photos(
            category_id,
            current_page,
            items_per_page,
            order_by
        )

    @staticmethod
    def get_photo(
            photo_id: int,
    ):
        qs = Queryset()
        return qs.get_photo(
            photo_id,
        )

    @staticmethod
    def like_dislike_photo(photo_id: int, action: str):
        qs = Queryset()
        return qs.like_dislike_photo(photo_id, action)
