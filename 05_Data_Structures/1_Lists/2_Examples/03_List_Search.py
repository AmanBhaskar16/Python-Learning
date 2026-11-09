# ==================================
# SEARCH ELEMENT IN LIST
# ==================================

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter number to search: "))

if target in numbers:
    print("Number Found!")
    print("Index:", numbers.index(target))

else:
    print("Number Not Found!")


# Find all occurrences

numbers = [10, 20, 10, 30, 10]

target = 10

for index, value in enumerate(numbers):

    if value == target:
        print("Found at index:", index)