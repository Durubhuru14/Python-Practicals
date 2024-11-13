# Simple example of using lambda functions in Python

# 1. A lambda function to add two numbers
add = lambda x, y: x + y
print("Sum of 3 and 5 is:", add(3, 5))  # Expected: 8

# 2. A lambda function to multiply two numbers
multiply = lambda x, y: x * y
print("Product of 4 and 6 is:", multiply(4, 6))  # Expected: 24

# 3. A lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print("Is 8 even?", is_even(8))  # Expected: True

# 4. A lambda function to get the square of a number
square = lambda x: x ** 2
print("Square of 5 is:", square(5))  # Expected: 25
