# ==================================
# LIST COMPREHENSION
# ==================================

# Normal Method

squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares) # [1, 4, 9, 16, 25]


# List Comprehension

squares = [i ** 2 for i in range(1, 6)] 

print(squares) # [1, 4, 9, 16, 25]


# Even Numbers

even = [i for i in range(1, 21) if i % 2 == 0]

print(even) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Odd Numbers

odd = [i for i in range(1, 21) if i % 2 != 0]

print(odd) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# Uppercase

names = ["rahul", "aman", "rohit"]

upper_names = [name.upper() for name in names]

print(upper_names) # ['RAHUL', 'AMAN', 'ROHIT']