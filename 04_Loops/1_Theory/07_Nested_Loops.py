# ==================================
# NESTED LOOPS
# ==================================

# Loop inside another loop

for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)


# Multiplication pattern

for i in range(1, 4):

    for j in range(1, 6):

        print(i * j, end=" ")

    print()