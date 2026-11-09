# SIMPLE MENU PROGRAM

print("===== FOOD MENU =====")
print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("You selected Pizza")

elif choice == 2:
    print("You selected Burger")

elif choice == 3:
    print("You selected Sandwich")

elif choice == 4:
    print("Thank you!")

else:
    print("Invalid Choice")