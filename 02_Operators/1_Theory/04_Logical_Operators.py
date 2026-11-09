# ==================================
# LOGICAL OPERATORS
# ==================================

a = 10
b = 20

# AND
print(a > 5 and b > 15)

# OR
print(a > 15 or b > 15)

# NOT
print(not(a > 5))


# Example: Login System

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Credentials")