from base_item import Item   
from item_types import Electronics, Clothing

class User:
    def __init__(self, name, premium_member=False):
        self.name = name
        self.premium_member = premium_member
        self.cart = []

    def add_to_cart(self, item, quantity=1):
        self.cart.append(item)
        print(f"{item} added to {self.name}'s cart.")
        item.update_stock(quantity)

    def view_cart(self):
        if not self.cart:
            print(f"{self.name}'s cart is empty.")
        else:
            print(f"{self.name}'s cart contains: {', '.join(str(item.name) for item in self.cart)}")

    def checkout(self):
        if not self.cart:
            print(f"{self.name}'s cart is empty. Cannot proceed to checkout.")
        else:
            print(f"{self.name} is checking out with items: {', '.join(str(item.name) for item in self.cart)}")
            self.cart.clear()