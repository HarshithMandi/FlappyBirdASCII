class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Item: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")

    def update_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError(f"Cannot update stock: only {self.stock} units available.")
        self.stock -= quantity
        print(f"Stock updated. Remaining stock: {self.stock} units")
    
                                                                    