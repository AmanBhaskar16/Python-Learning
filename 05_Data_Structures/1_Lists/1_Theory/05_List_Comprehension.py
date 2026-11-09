# ==================================
# LIST COMPREHENSION
# ==================================

# Normal Method

squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)


# List Comprehension

squares = [i ** 2 for i in range(1, 6)]

print(squares)


# Even Numbers

even = [i for i in range(1, 21) if i % 2 == 0]

print(even)


# Odd Numbers

odd = [i for i in range(1, 21) if i % 2 != 0]

print(odd)


# Uppercase

names = ["rahul", "aman", "rohit"]

upper_names = [name.upper() for name in names]

print(upper_names)