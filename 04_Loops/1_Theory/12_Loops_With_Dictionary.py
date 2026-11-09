# ==================================
# LOOPS WITH DICTIONARY
# ==================================

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Arrah"
}


# Keys

for key in student:
    print(key)


# Values

for value in student.values():
    print(value)


# Keys and Values

for key, value in student.items():
    print(key, ":", value)