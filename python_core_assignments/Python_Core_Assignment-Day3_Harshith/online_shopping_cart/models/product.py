class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self._name = name
        self._price = float(price)
        self._stock = int(stock)

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    def reduce_stock(self, quantity: int) -> None:
        self._stock -= quantity

    def increase_stock(self, quantity: int) -> None:
        self._stock += quantity

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"
