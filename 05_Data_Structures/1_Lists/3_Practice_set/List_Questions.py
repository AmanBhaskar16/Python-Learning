# ==================================
# LIST PRACTICE QUESTIONS
# ==================================

# Q1. Create a list of 10 numbers.
nums = [5, 12, 7, 3, 9, 15, 2, 8, 10, 4]

print("Original list:", nums)


# Q2. Find the largest number in a list.
maxi = nums[0]

for num in nums:
    if num > maxi:
        maxi = num

print("Largest number:", maxi)


# Q3. Find the smallest number in a list.
mini = nums[0]

for num in nums:
    if num < mini:
        mini = num

print("Smallest number:", mini)


# Q4. Calculate the sum of all list elements.
total = 0

for num in nums:
    total += num

print("Sum:", total)


# Q5. Calculate the average of list elements.
average = total / len(nums)

print("Average:", average)


# Q6. Reverse a list without using reverse().
print("Reversed list:")

for i in range(len(nums) - 1, -1, -1):
    print(nums[i], end=" ")

print()


# Q7. Remove duplicate elements from a list.
nums = [1, 2, 3, 2, 4, 3, 5, 1]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)


# Q8. Find the second largest distinct number.
largest = nums[0]
second_largest = None

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num < largest:
        if second_largest is None or num > second_largest:
            second_largest = num

print("Second largest:", second_largest)


# Q9. Sort a list in ascending order.
nums = [5, 2, 8, 1, 9, 3]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print("Sorted list:", nums)


# Q10. Count even and odd numbers in a list.
nums = [1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# Q11. Find common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)


# Q12. Create a shopping list program.
shopping_list = []

while True:
    print("\n1. Add item")
    print("2. View shopping list")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added!")

    elif choice == "2":
        print("Shopping list:", shopping_list)

    elif choice == "3":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed!")
        else:
            print("Item not found.")

    elif choice == "4":
        print("Exiting shopping list program.")
        break

    else:
        print("Invalid choice.")