# ==================================
# NESTED DICTIONARY
# ==================================

students = {

    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },

    "student2": {
        "name": "Aman",
        "age": 21,
        "marks": 90
    },

    "student3": {
        "name": "Priya",
        "age": 19,
        "marks": 95
    }
}


# Display All Students

for student_id, details in students.items():

    print("\nStudent ID:", student_id)

    for key, value in details.items():
        print(key, ":", value)


# Access Particular Student

print("\nRahul's Marks:")
print(students["student1"]["marks"])


# Update Marks

students["student1"]["marks"] = 95

print("\nUpdated Marks:")
print(students["student1"]["marks"])