# Check Prime Number

number = int(input("Enter a number: "))

if number <= 1:
    print("Not a Prime Number")

else:

    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")

    else:
        print("Not a Prime Number")


# Print prime numbers from 1 to 100

for num in range(2, 101):

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)