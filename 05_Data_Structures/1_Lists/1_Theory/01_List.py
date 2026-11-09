# ==================================
# PYTHON LIST
# ==================================

# List stores multiple values.

fruits = ["Apple", "Mango", "Banana"]

print(fruits)

# Access elements
print(fruits[0]) # Apple
print(fruits[1]) # Mango

# Modify elements
fruits[0] = "Orange" 

print(fruits) # ['Orange', 'Mango', 'Banana']

# Add elements
fruits.append("Grapes") 

print(fruits) # ['Orange', 'Mango', 'Banana', 'Grapes']

# Remove elements
fruits.remove("Mango")

print(fruits) # ['Orange', 'Banana', 'Grapes']

# List can store different data types

data = [10, 20.5, "Python", True]

print(data) # [10, 20.5, 'Python', True]

# Duplicate values are allowed

numbers = [10, 20, 10, 30]

print(numbers) # [10, 20, 10, 30]

# List length
print(len(fruits)) # 3