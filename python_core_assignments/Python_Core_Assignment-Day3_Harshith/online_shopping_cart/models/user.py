from models.cart import Cart


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cart = Cart()
