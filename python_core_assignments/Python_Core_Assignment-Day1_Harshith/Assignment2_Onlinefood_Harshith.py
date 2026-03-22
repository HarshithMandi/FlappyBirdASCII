orders = {}

def add_order():
    order_id = input("Enter Order ID: ")
    if order_id in orders:
        print("Order ID already exists.")
        return
    name = input("Enter Customer Name: ")
    orders[order_id] = {"customer": name, "items": {}}
    print("Order created successfully")

def add_food_item():
    order_id = input("Enter Order ID: ")
    if order_id not in orders:
        print("Order not found.")
        return
    item = input("Enter food item: ")
    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price.")
        return
    orders[order_id]["items"][item] = price
    print("Item added to order")

def remove_food_item():
    order_id = input("Enter Order ID: ")
    if order_id not in orders:
        print("Order not found.")
        return
    item = input("Enter item to remove: ")
    if item in orders[order_id]["items"]:
        del orders[order_id]["items"][item]
        print("Item removed from order")
    else:
        print("Item not found in order.")

def display_all_orders():
    if not orders:
        print("No orders found.")
        return
    for order_id, details in orders.items():
        total = sum(details["items"].values())
        print(f"\nOrder ID: {order_id}")
        print(f"Customer: {details['customer']}")
        print(f"Items: {list(details['items'].keys())}")
        print(f"Total Bill: {total}")

def search_order():
    order_id = input("Enter Order ID to search: ")
    if order_id not in orders:
        print("Order not found.")
        return
    details = orders[order_id]
    total = sum(details["items"].values())
    print(f"\nOrder ID: {order_id}")
    print(f"Customer: {details['customer']}")
    print(f"Items: {list(details['items'].keys())}")
    print(f"Total Bill: {total}")

def remove_order():
    order_id = input("Enter Order ID to remove after delivery: ")
    if order_id in orders:
        del orders[order_id]
        print("Order removed successfully.")
    else:
        print("Order not found.")

while True:
    print("\n===== Online Food Delivery Order Management =====")
    print("1. Add a New Order")
    print("2. Add Food Items to an Order")
    print("3. Remove an Item from an Order")
    print("4. Display All Orders")
    print("5. Search Order by Order ID")
    print("6. Remove an Order after Delivery")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_order()
    elif choice == '2':
        add_food_item()
    elif choice == '3':
        remove_food_item()
    elif choice == '4':
        display_all_orders()
    elif choice == '5':
        search_order()
    elif choice == '6':
        remove_order()
    elif choice == '7':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
