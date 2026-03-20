from models.order import Order
from typing import Optional
from pymongo.collection import Collection

class OrderRepository:
    def __init__(self, collection: Collection):
        self.collection = collection
    def get_by_id(self,id: str) -> Optional[Order]:
        data = self.collection.find_one({"_id": id})
        return Order(**data) if data else None
    def create(self, order: Order) -> Order:
        result = self.collection.insert_one(order.dict())
        return str(result.inserted_id)