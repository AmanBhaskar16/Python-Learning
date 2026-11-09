# ==================================
# PYTHON SET
# ==================================

# Set stores unique elements.

numbers = {10, 20, 30, 10, 20}

print(numbers)

# Duplicate values automatically removed.

# Add Element
numbers.add(40)

print(numbers)

# Update
numbers.update([50, 60, 70])

print(numbers)

# Remove
numbers.remove(20)

print(numbers)

# Discard
numbers.discard(100)

print(numbers)

# Pop
numbers.pop()

print(numbers)

# Length
print(len(numbers))

# Empty Set
empty_set = set()

print(type(empty_set))

# Important:
# Empty {} creates a dictionary, not a set.