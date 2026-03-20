from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

class Database:
    client: AsyncIOMotorClient = None

    @classmethod
    def connect(cls):
        cls.client = AsyncIOMotorClient(settings.MONGODB_URI)

    @classmethod
    def disconnect(cls):
        if cls.client is not None:
            cls.client.close()
            cls.client = None

    @classmethod
    def get_db(cls):
        return cls.client[settings.DB_NAME]
