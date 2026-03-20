from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.order_repository import OrderRepository
from services.user_service import UserService
from services.product_service import ProductService
from services.order_service import OrderService
from core.database import Database

def get_user_repository() -> UserRepository:
    db = Database().get_db()
    return UserRepository(db["users"])

def get_product_repository() -> ProductRepository:
    db = Database().get_db()
    return ProductRepository(db["products"])

def get_order_repository() -> OrderRepository:
    db = Database().get_db()
    return OrderRepository(db["orders"])

def get_user_service() -> UserService:
    return UserService(get_user_repository())

def get_product_service() -> ProductService:
    return ProductService(get_product_repository())

def get_order_service() -> OrderService:
    return OrderService(get_order_repository())