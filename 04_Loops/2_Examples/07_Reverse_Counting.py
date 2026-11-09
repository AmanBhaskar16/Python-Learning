# Reverse Counting

for i in range(10, 0, -1):
    print(i)


# Reverse a number

number = int(input("Enter a number: "))

reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number //= 10

print("Reverse:", reverse)