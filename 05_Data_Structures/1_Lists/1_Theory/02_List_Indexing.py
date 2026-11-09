# ==================================
# LIST INDEXING
# ==================================

numbers = [10, 20, 30, 40, 50]

# Positive Indexing
print(numbers[0]) # 10
print(numbers[1]) # 20
print(numbers[2]) # 30

# Negative Indexing
print(numbers[-1]) # 50
print(numbers[-2]) # 40
print(numbers[-3]) # 30

# First Element
print(numbers[0]) # 10

# Last Element
print(numbers[-1]) # 50

# Update Element
numbers[2] = 100

print(numbers) # [10, 20, 100, 40, 50]

# Index Error Example
# print(numbers[10]) # Error