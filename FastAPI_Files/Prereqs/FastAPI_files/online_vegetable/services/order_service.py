from models.order import Order
from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderCreate


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, order_data: OrderCreate) -> Order:
        order = Order(**order_data.dict(), status="pending")
        return self.order_repository.create(order)

    def get_order(self, id: str) -> Order:
        return self.order_repository.get_by_id(id)