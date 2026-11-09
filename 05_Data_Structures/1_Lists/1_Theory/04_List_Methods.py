# ==================================
# LIST METHODS
# ==================================

numbers = [10, 20, 30]

# Append
numbers.append(40)
print(numbers) # [10, 20, 30, 40]

# Extend
numbers.extend([50, 60])
print(numbers) # [10, 20, 30, 40, 50, 60]

# Insert
numbers.insert(1, 15)
print(numbers) # [10, 15, 20, 30, 40, 50, 60]

# Remove
numbers.remove(30)
print(numbers) # [10, 15, 20, 40, 50, 60]

# Pop
numbers.pop()
print(numbers) # [10, 15, 20, 40, 50]

# Sort
numbers.sort()
print(numbers) # [10, 15, 20, 40, 50]

# Reverse
numbers.reverse()
print(numbers) # [50, 40, 20, 15, 10]

# Count
print(numbers.count(10)) # 1

# Index
print(numbers.index(20)) # 2

# Copy
new_numbers = numbers.copy()
print(new_numbers) # [50, 40, 20, 15, 10]

# Clear
numbers.clear()
print(numbers) # []