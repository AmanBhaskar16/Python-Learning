# ==================================
# LOOPS WITH LIST
# ==================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# Sum of list

total = 0

for num in numbers:
    total += num

print("Total:", total)


# List with index

for index, value in enumerate(numbers):
    print(index, value)