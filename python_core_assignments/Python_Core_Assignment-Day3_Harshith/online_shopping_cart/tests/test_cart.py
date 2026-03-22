import tempfile
import unittest
from pathlib import Path

from exceptions.cart_exceptions import OutOfStockError, ProductNotFoundError
from models.premium_user import PremiumUser
from models.user import User
from services.cart_service import CartService
from services.store_service import StoreService


class TestCartSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.store = StoreService()
        self.store.add_product("Laptop", 1000, 5)
        self.store.add_product("Mouse", 25, 10)
        self.cart_service = CartService(self.store)
        self.user = User("Alice")

    def test_add_product(self):
        self.cart_service.add_to_cart(self.user, "Laptop", 1)
        self.assertEqual(len(self.user.cart.items), 1)
        self.assertEqual(self.user.cart.get_total(), 1000)

    def test_add_product_out_of_stock(self):
        with self.assertRaises(OutOfStockError):
            self.cart_service.add_to_cart(self.user, "Laptop", 10)

    def test_remove_product(self):
        self.cart_service.add_to_cart(self.user, "Mouse", 2)
        self.cart_service.remove_from_cart(self.user, "Mouse", 1)
        self.assertEqual(self.user.cart.items["Mouse"]["quantity"], 1)

    def test_remove_missing_product(self):
        with self.assertRaises(ProductNotFoundError):
            self.cart_service.remove_from_cart(self.user, "Tablet", 1)

    def test_checkout_clears_cart(self):
        self.cart_service.add_to_cart(self.user, "Mouse", 2)
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            path = Path(tmp.name)
        total = self.cart_service.checkout(self.user, path)
        self.assertEqual(total, 50)
        self.assertEqual(len(self.user.cart.items), 0)
        path.unlink(missing_ok=True)

    def test_premium_user_discount_on_checkout(self):
        premium = PremiumUser("Bob", discount_rate=0.10)
        self.cart_service.add_to_cart(premium, "Laptop", 1)
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            path = Path(tmp.name)
        total = self.cart_service.checkout(premium, path)
        self.assertEqual(total, 900)
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
