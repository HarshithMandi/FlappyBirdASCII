from models.product import Product
from typing import Optional
from pymongo.collection import Collection


class ProductRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_by_id(self, id: str) -> Optional[Product]:
        data = self.collection.find_one({"_id": id})
        return Product(**data) if data else None

    def create(self, product: Product) -> Product:
        result = self.collection.insert_one(product.dict())
        return str(result.inserted_id)