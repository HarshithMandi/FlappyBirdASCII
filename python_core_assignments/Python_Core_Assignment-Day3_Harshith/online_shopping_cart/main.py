from exceptions.cart_exceptions import (
    InvalidQuantityError,
    OutOfStockError,
    ProductNotFoundError,
)
from models.premium_user import PremiumUser
from models.user import User
from services.cart_service import CartService
from services.store_service import StoreService


def print_products(store: StoreService) -> None:
    print("\nAvailable Products")
    print("-" * 45)
    print(f"{'Name':<15} {'Price':<10} {'Stock':<10}")
    print("-" * 45)
    for product in store.list_products():
        print(f"{product.name:<15} {product.price:<10.2f} {product.stock:<10}")


def print_cart(user: User) -> None:
    items = user.cart.view_cart()
    if not items:
        print("Cart is empty")
        return

    print("\nCart Items")
    print("-" * 55)
    print(f"{'Name':<15} {'Qty':<10} {'Price':<10} {'Subtotal':<10}")
    print("-" * 55)
    for item in items:
        print(
            f"{item['name']:<15} {item['quantity']:<10} "
            f"{item['price']:<10.2f} {item['subtotal']:<10.2f}"
        )
    print("-" * 55)
    print(f"Total: {user.cart.get_total():.2f}")


if __name__ == "__main__":
    store = StoreService()
    store.add_product("Laptop", 1000, 5)
    store.add_product("Mouse", 25, 20)
    store.add_product("Keyboard", 45, 15)

    user_type = input("Enter user type (normal/premium): ").strip().lower()
    user_name = input("Enter user name: ").strip()
    user = PremiumUser(user_name) if user_type == "premium" else User(user_name)

    cart_service = CartService(store)

    while True:
        print("\n===== Online Shopping Cart System =====")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                print_products(store)
            elif choice == "2":
                name = input("Enter product name: ").strip()
                qty = int(input("Enter quantity: ").strip())
                cart_service.add_to_cart(user, name, qty)
                print("Product added to cart")
            elif choice == "3":
                name = input("Enter product name: ").strip()
                qty_input = input("Enter quantity to remove (blank for all): ").strip()
                qty = int(qty_input) if qty_input else None
                cart_service.remove_from_cart(user, name, qty)
                print("Product removed from cart")
            elif choice == "4":
                print_cart(user)
            elif choice == "5":
                total = cart_service.checkout(user)
                print(f"Order placed successfully. Final total: {total:.2f}")
            elif choice == "6":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice")

        except (ProductNotFoundError, OutOfStockError, InvalidQuantityError, ValueError) as error:
            print(error)
