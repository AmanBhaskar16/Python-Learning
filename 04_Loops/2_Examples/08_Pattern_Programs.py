# ==================================
# PATTERN PROGRAMS
# ==================================

# Pattern 1

for i in range(1, 6):
    print("*" * i)


# Pattern 2

for i in range(5, 0, -1):
    print("*" * i)


# Pattern 3

for i in range(1, 6):
    print(str(i) * i)


# Pattern 4

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# Pattern 5: Pyramid

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)