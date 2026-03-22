from exceptions.cart_exceptions import ProductNotFoundError
from models.premium_user import PremiumUser
from models.user import User
from services.store_service import StoreService
from utils.file_handler import save_order


class CartService:
    def __init__(self, store_service: StoreService) -> None:
        self.store_service = store_service

    def add_to_cart(self, user: User, product_name: str, quantity: int) -> None:
        product = self.store_service.get_product(product_name)
        user.cart.add_product(product, quantity)

    def remove_from_cart(self, user: User, product_name: str, quantity: int | None = None) -> None:
        user.cart.remove_product(product_name, quantity)

    def checkout(self, user: User, order_file_path=None) -> float:
        cart_items = user.cart.view_cart()
        if not cart_items:
            raise ProductNotFoundError("Cart is empty")

        total = user.cart.get_total()
        if isinstance(user, PremiumUser):
            total = user.get_discounted_total(total)

        save_order(user.name, cart_items, total, order_file_path)
        user.cart.clear()
        return total
