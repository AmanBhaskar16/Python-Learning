# ==================================
# SET OPERATIONS
# ==================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print(a.union(b))

# Intersection
print(a.intersection(b))

# Difference
print(a.difference(b))

# Symmetric Difference
print(a.symmetric_difference(b))

# Subset
print({1, 2}.issubset(a))

# Superset
print(a.issuperset({1, 2}))

# Disjoint
print({10, 20}.isdisjoint(a))

# Operators

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric Difference