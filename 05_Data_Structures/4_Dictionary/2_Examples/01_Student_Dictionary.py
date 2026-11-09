# ==================================
# STUDENT MANAGEMENT
# ==================================

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python",
    "marks": 85
}

# Display Information

for key, value in student.items():
    print(key, ":", value)


# Update Marks

student["marks"] = 95

# Add City

student["city"] = "Arrah"

# Display Updated Information

print("\nUpdated Student:")

for key, value in student.items():
    print(key, ":", value)