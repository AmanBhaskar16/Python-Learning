# ==================================
# SHOPPING LIST
# ==================================

shopping_list = []

while True:

    print("\n1. Add Item")
    print("2. View Items")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter item: ")
        shopping_list.append(item)

        print("Item Added!")

    elif choice == "2":

        for item in shopping_list:
            print("-", item)

    elif choice == "3":

        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print("Item Removed!")
        else:
            print("Item Not Found!")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")