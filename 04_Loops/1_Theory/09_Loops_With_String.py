# ==================================
# LOOPS WITH STRING
# ==================================

name = "Python"

for char in name:
    print(char)


# Count characters

count = 0

for char in name:
    count += 1

print("Characters:", count)


# Count vowels

text = "programming"
vowels = "aeiou"
count = 0

for char in text:

    if char in vowels:
        count += 1

print("Vowels:", count)