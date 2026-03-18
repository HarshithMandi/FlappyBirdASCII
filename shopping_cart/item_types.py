from base_item import Item

class Electronics(Item):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years

    def display_info(self):
        super().display_info()
        print(f"Warranty: {self.warranty_years} years")

class Clothing(Item):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
        

