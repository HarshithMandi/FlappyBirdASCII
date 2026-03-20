from typing import Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection

from models.user import User


class UserRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def get_by_email(self, email: str) -> Optional[User]:
        data = await self.collection.find_one({"email": email})
        return self._to_model(data)

    async def create(self, user: User) -> str:
        payload = user.dict(exclude_none=True)
        payload.pop("id", None)
        result = await self.collection.insert_one(payload)
        return str(result.inserted_id)

    @staticmethod
    def _to_model(data: Optional[dict]) -> Optional[User]:
        if not data:
            return None
        if "_id" in data:
            data = {**data, "id": str(data["_id"])}
            data.pop("_id", None)
        return User(**data)