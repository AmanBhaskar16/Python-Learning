# ==================================
# REMOVE DUPLICATES
# ==================================

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

# Using Set

unique_numbers = list(set(numbers))

print("Original:", numbers)
print("Unique:", unique_numbers)


# Preserve Original Order

unique_numbers = list(dict.fromkeys(numbers))

print("Order Preserved:", unique_numbers)