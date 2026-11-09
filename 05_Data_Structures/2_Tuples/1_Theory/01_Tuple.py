# ==================================
# PYTHON TUPLE
# ==================================

# Tuple is ordered and immutable.

fruits = ("Apple", "Mango", "Banana")

print(fruits)

# Access Elements
print(fruits[0])
print(fruits[-1])

# Tuple Length
print(len(fruits))

# Duplicate Values
numbers = (10, 20, 10, 30)

print(numbers)

# Mixed Data Types
data = (10, "Python", 20.5, True)

print(data)

# Single Element Tuple
single = (10,)

print(type(single))

# Tuple without parentheses
values = 10, 20, 30

print(values)
print(type(values))

# Tuple is immutable
# fruits[0] = "Orange"  # TypeError