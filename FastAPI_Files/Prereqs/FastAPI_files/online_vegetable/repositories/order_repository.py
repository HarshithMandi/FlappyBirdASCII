from models.order import Order
from typing import Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection

class OrderRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def get_by_id(self, id: str) -> Optional[Order]:
        try:
            oid = ObjectId(id)
        except Exception:
            return None

        data = await self.collection.find_one({"_id": oid})
        return self._to_model(data)

    async def create(self, order: Order) -> str:
        payload = order.dict(exclude_none=True)
        payload.pop("id", None)
        result = await self.collection.insert_one(payload)
        return str(result.inserted_id)

    @staticmethod
    def _to_model(data: Optional[dict]) -> Optional[Order]:
        if not data:
            return None
        if "_id" in data:
            data = {**data, "id": str(data["_id"])}
            data.pop("_id", None)
        return Order(**data)