# ==================================
# STUDENT LIST MANAGEMENT
# ==================================

students = []

# Add Students

students.append("Rahul")
students.append("Aman")
students.append("Rohit")
students.append("Priya")

print("Students:", students)

# Display Students

for student in students:
    print(student)

# Search Student

name = input("Enter student name: ")

if name in students:
    print("Student Found!")
else:
    print("Student Not Found!")

# Remove Student

remove_name = input("Enter name to remove: ")

if remove_name in students:
    students.remove(remove_name)
    print("Student Removed!")

print("Final List:", students)