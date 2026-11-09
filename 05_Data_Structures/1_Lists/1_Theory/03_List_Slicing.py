# ==================================
# LIST SLICING
# ==================================

numbers = [10, 20, 30, 40, 50, 60]

# Basic Slicing
print(numbers[1:4]) # [20, 30, 40] , start index is inclusive and end index is exclusive

# From Starting
print(numbers[:3]) # [10, 20, 30] , start index is 0 by default and end index is exclusive

# Till Ending
print(numbers[2:]) # [30, 40, 50, 60] , start index is inclusive and end index is last index by default

# Complete List
print(numbers[:]) # [10, 20, 30, 40, 50, 60] , start index is 0 by default and end index is last index by default

# Step Slicing
print(numbers[::2]) # [10, 30, 50] , step index is 2, so it takes every second element from the list

# Reverse List
print(numbers[::-1]) # [60, 50, 40, 30, 20, 10] , step index is -1, so it takes every element from the list in reverse order

# Negative Slicing
print(numbers[-4:-1]) # [30, 40, 50] , starts from -4 and goes till -2 