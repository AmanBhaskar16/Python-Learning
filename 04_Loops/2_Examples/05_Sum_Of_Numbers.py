# Sum of numbers from 1 to N

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Total Sum:", total)


# Sum of digits

number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)