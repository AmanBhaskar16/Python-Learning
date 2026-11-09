# ==================================
# TUPLE METHODS
# ==================================

numbers = (10, 20, 30, 10, 40, 10)

# Count
print(numbers.count(10))

# Index
print(numbers.index(30))

# Length
print(len(numbers))

# Maximum
print(max(numbers))

# Minimum
print(min(numbers))

# Sum
print(sum(numbers))

# Convert Tuple into List

new_list = list(numbers)

print(new_list)

# Modify List
new_list.append(50)

print(new_list)

# Convert List into Tuple

new_tuple = tuple(new_list)

print(new_tuple)