# ==================================
# LIST METHODS
# ==================================

numbers = [10, 20, 30]

# Append
numbers.append(40)
print(numbers)

# Extend
numbers.extend([50, 60])
print(numbers)

# Insert
numbers.insert(1, 15)
print(numbers)

# Remove
numbers.remove(30)
print(numbers)

# Pop
numbers.pop()
print(numbers)

# Sort
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# Count
print(numbers.count(10))

# Index
print(numbers.index(20))

# Copy
new_numbers = numbers.copy()
print(new_numbers)

# Clear
numbers.clear()
print(numbers)