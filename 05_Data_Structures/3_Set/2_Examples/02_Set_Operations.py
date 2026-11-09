# ==================================
# SET OPERATIONS EXAMPLE
# ==================================

python_students = {"Rahul", "Aman", "Priya", "Rohit"}

java_students = {"Aman", "Rohit", "Karan", "Vikas"}

# Students learning either language

all_students = python_students | java_students

print("All Students:", all_students)


# Students learning both languages

common_students = python_students & java_students

print("Common Students:", common_students)


# Only Python Students

only_python = python_students - java_students

print("Only Python:", only_python)


# Only one of the two languages

only_one = python_students ^ java_students

print("Only One Language:", only_one)