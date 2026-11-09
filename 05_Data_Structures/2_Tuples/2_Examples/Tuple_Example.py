# ==================================
# STUDENT RECORD USING TUPLE
# ==================================

student = ("Rahul", 20, "Python", 85.5)

name, age, course, marks = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)


# Multiple Students

students = (
    ("Rahul", 85),
    ("Aman", 90),
    ("Priya", 95)
)

for name, marks in students:

    print(name, marks)