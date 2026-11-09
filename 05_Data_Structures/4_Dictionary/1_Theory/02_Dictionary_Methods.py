# ==================================
# DICTIONARY METHODS
# ==================================

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Arrah"
}

# Keys
print(student.keys())

# Values
print(student.values())

# Items
print(student.items())

# Get
print(student.get("name"))

# Update
student.update({"age": 21})

print(student)

# Set Default
student.setdefault("course", "Python")

print(student)

# Pop
student.pop("city")

print(student)

# Popitem
student.popitem()

print(student)

# Copy
new_student = student.copy()

print(new_student)

# Clear
student.clear()

print(student)