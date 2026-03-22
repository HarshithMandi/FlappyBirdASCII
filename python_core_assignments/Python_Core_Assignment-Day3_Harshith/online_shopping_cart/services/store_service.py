from exceptions.cart_exceptions import ProductNotFoundError
from models.product import Product


class StoreService:
    def __init__(self) -> None:
        self.products: dict[str, Product] = {}

    def add_product(self, name: str, price: float, stock: int) -> None:
        self.products[name] = Product(name, price, stock)

    def get_product(self, name: str) -> Product:
        product = self.products.get(name)
        if not product:
            raise ProductNotFoundError("Product not found")
        return product

    def list_products(self) -> list[Product]:
        return list(self.products.values())
