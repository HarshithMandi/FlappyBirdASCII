from models.order import Order
from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderCreate


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    async def create_order(self, order_data: OrderCreate) -> str:
        order = Order(**order_data.dict(), status="pending")
        return await self.order_repository.create(order)

    async def get_order(self, id: str) -> Order:
        return await self.order_repository.get_by_id(id)

    async def get_order_by_id(self, order_id: str) -> Order:
        return await self.get_order(order_id)