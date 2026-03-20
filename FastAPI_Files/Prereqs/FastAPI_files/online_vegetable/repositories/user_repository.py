from models.product import Product
from typing import Optional
from pymongo.collection import Collection


class UserRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_by_email(self, email: str) -> Optional[Product]:
        data = self.collection.find_one({"email": email})
        return Product(**data) if data else None

    def create(self, product: Product) -> Product:
        result = self.collection.insert_one(product.dict())
        return str(result.inserted_id)