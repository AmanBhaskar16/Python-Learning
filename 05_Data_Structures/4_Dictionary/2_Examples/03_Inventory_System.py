# ==================================
# INVENTORY MANAGEMENT SYSTEM
# ==================================

inventory = {
    "Laptop": 10,
    "Mobile": 20,
    "Keyboard": 15,
    "Mouse": 30
}

while True:

    print("\n===== INVENTORY =====")
    print("1. View Inventory")
    print("2. Add Stock")
    print("3. Sell Product")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        for product, quantity in inventory.items():
            print(product, ":", quantity)

    elif choice == "2":

        product = input("Enter product: ")
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive!")

        else:
            inventory[product] = inventory.get(product, 0) + quantity
            print("Stock Added!")

    elif choice == "3":

        product = input("Enter product: ")
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive!")

        elif product not in inventory:
            print("Product Not Found!")

        elif inventory[product] < quantity:
            print("Insufficient Stock!")

        else:
            inventory[product] -= quantity
            print("Product Sold!")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")