# ==================================
# SET METHODS
# ==================================

numbers = {10, 20, 30, 40}

# Add
numbers.add(50)
print(numbers)

# Update
numbers.update([60, 70])
print(numbers)

# Remove
numbers.remove(20)
print(numbers)

# Discard
numbers.discard(100)
print(numbers)

# Copy
new_set = numbers.copy()
print(new_set)

# Difference Update
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)
print(a)

# Intersection Update
a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)
print(a)

# Clear
numbers.clear()
print(numbers)