# ==================================
# CONTINUE STATEMENT
# ==================================

# Skip even numbers

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)


# Skip a particular number

for i in range(1, 6):

    if i == 3:
        continue

    print(i)