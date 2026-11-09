# ==================================
# PYTHON DICTIONARY
# ==================================

# Dictionary stores key-value pairs.

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Arrah"
}

print(student)

# Access Value
print(student["name"])

# Get Method
print(student.get("age"))

# Add New Key
student["course"] = "Python"

print(student)

# Update Value
student["age"] = 21

print(student)

# Remove Key
student.pop("city")

print(student)

# Check Key
print("name" in student)

# Length
print(len(student))

# Dictionary Keys must be unique.