from exceptions.cart_exceptions import InvalidQuantityError, OutOfStockError, ProductNotFoundError
from models.product import Product


class Cart:
    def __init__(self) -> None:
        self.items: dict[str, dict] = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")
        if product.stock < quantity:
            raise OutOfStockError("Requested quantity exceeds available stock")

        product.reduce_stock(quantity)

        if product.name in self.items:
            self.items[product.name]["quantity"] += quantity
        else:
            self.items[product.name] = {"product": product, "quantity": quantity}

    def remove_product(self, product_name: str, quantity: int | None = None) -> None:
        if product_name not in self.items:
            raise ProductNotFoundError("Product not found in cart")

        if quantity is None:
            quantity = self.items[product_name]["quantity"]
        assert quantity is not None

        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")

        current_quantity = self.items[product_name]["quantity"]
        if quantity >= current_quantity:
            self.items[product_name]["product"].increase_stock(current_quantity)
            del self.items[product_name]
            return

        self.items[product_name]["quantity"] -= quantity
        self.items[product_name]["product"].increase_stock(quantity)

    def view_cart(self) -> list[dict]:
        return [
            {
                "name": item_name,
                "price": item_data["product"].price,
                "quantity": item_data["quantity"],
                "subtotal": round(item_data["product"].price * item_data["quantity"], 2),
            }
            for item_name, item_data in self.items.items()
        ]

    def get_total(self) -> float:
        return round(
            sum(item["product"].price * item["quantity"] for item in self.items.values()),
            2,
        )

    def clear(self) -> None:
        self.items.clear()
