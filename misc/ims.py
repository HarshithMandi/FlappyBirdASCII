# Warehouse inventory management system
inventory=[]
while True:
    choice=int(input("choice: \n1.Add new products\n2.insert urgent products\n3.combine products from another warehouse\n4.remove discontinued products\n5.process shipped products\n6.count product occurences\n7.find product positions\n8.sort products\n9.reverse display order\n10.create a backup copy\n11."))
    if choice==1:
        product=input("Enter the product name to add: ")
        inventory.append(product)
        print(f"{product} added to inventory.")
    elif choice== 2:
        product=input("Enter the urgent product name to insert: ")
        inventory.insert(0,product)
        print(f"{product} inserted at the beginning of inventory.") 
    elif choice== 3:
        other_warehouse=["ProductA","ProductB","ProductC"]
        inventory.extend(other_warehouse)
        print("Products from another warehouse combined.")
    elif choice== 4:
        product=input("Enter the discontinued product name to remove: ")
        if product in inventory:
            inventory.remove(product)
            print(f"{product} removed from inventory.")
        else:
            print(f"{product} not found in inventory.")
    elif choice== 5:
        product=input("Enter the shipped product name to process: ")
        if product in inventory:
            inventory.remove(product)
            print(f"{product} processed as shipped.")
        else:
            print(f"{product} not found in inventory.")
    elif choice== 6:
        product=input("Enter the product name to count occurrences: ")
        count=inventory.count(product)
        print(f"{product} occurs {count} times in inventory.")
    elif choice== 7:
        product=input("Enter the product name to find positions: ")
        positions=[index for index, value in enumerate(inventory) if value==product]
        if positions:
            print(f"{product} found at positions: {positions}")
        else:
            print(f"{product} not found in inventory.")
    elif choice== 8:
        inventory.sort()
        print("Inventory sorted.")
    elif choice== 9:
        inventory.reverse()
        print("Inventory display order reversed.")
    elif choice== 10:
        backup_inventory=inventory.copy()
        print("Backup copy of inventory created.")
    elif choice== 11:
        print("Exiting the inventory management system.")
        break