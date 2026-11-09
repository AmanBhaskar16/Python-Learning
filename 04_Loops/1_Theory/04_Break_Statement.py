# ==================================
# BREAK STATEMENT
# ==================================

# Break stops the loop immediately.

for i in range(1, 11):

    if i == 5:
        break

    print(i)


# Search an element

numbers = [10, 20, 30, 40, 50]

for num in numbers:

    if num == 30:
        print("Number Found!")
        break

    print(num)