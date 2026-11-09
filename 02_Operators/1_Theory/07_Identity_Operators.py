# ==================================
# IDENTITY OPERATORS
# ==================================

a = [1, 2, 3]
b = [1, 2, 3]

c = a

# == checks values
print(a == b)

# is checks object identity
print(a is b)

print(a is c)

# is not
print(a is not b)


# None checking
value = None

print(value is None)