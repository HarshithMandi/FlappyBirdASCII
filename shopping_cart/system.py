from base_item import Item
from item_types import Electronics, Clothing
from cart import User


if __name__ == "__main__":
    laptop = Electronics("Laptop", 999.99, 10, 2)
    tshirt = Clothing("T-Shirt", 19.99, 50, "M")

    laptop.display_info()
    print()
    tshirt.display_info()
    print()

    user = User("Alice", premium_member=True)
    user.add_to_cart(laptop, quantity=1)
    user.add_to_cart(tshirt, quantity=2)

    user.view_cart()

    user.checkout()