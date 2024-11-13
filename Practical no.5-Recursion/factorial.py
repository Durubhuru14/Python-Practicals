# Taking user input for a positive integer greater than zero
n = int(input("Enter a positive integer greater than zero: "))

# Function to calculate the factorial of a number using recursion
def factorial(n):
    # Base case: If n is 1, return 1 (factorial of 1 is 1)
    if n == 1:
        return n
    else:
        # Recursive case: Multiply n with factorial of (n-1)
        return n * factorial(n - 1)

# Checking if the input number is a positive integer greater than zero
if n > 0:
    # Output the result of factorial
    print(f"Factorial of number {n} is {factorial(n)}")
else:
    # If the input is not valid (i.e., less than or equal to zero)
    print("Please enter a positive integer greater than zero.")
