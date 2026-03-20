from motor.motor_asyncio import AsyncIOMotorClient
from core.config import Settings,settings
from fastapi import FastAPI

class Database:
    client: AsyncIOMotorClient = None

    @classmethod
    def connect(cls):
        cls.client = AsyncIOMotorClient(settings.MONGODB_URI)

    @classmethod
    def get_db(cls):
        return cls.client[settings.DB_NAME]
