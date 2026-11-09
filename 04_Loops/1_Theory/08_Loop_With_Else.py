# ==================================
# LOOP WITH ELSE
# ==================================

# Else executes when loop completes normally.

for i in range(1, 6):
    print(i)

else:
    print("Loop Completed")


# Else does not execute after break.

for i in range(1, 6):

    if i == 3:
        break

    print(i)

else:
    print("This will not print")