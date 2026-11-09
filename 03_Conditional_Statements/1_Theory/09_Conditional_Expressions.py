# ==================================
# CONDITIONAL EXPRESSIONS
# ==================================

temperature = 35

if temperature > 30:
    message = "Hot Weather"
else:
    message = "Normal Weather"

print(message)


# Multiple conditions

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "Fail"

print("Grade:", grade)