# math_functions.py
# This program defines and calls functions to solve specific problems.
# It includes two functions: one to calculate the factorial of a number
# and another to check if a number is prime.

def factorial(n):
    """
    Calculate the factorial of a number.
    :param n: Integer for which factorial is to be calculated
    :return: Factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is prime.
    :param n: Integer to check for primality
    :return: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Main program
def main():
    # Input a number from the user
    number = int(input("Enter a number: "))

    # Call the factorial function and display the result
    print(f"The factorial of {number} is {factorial(number)}")

    # Call the is_prime function and display if the number is prime or not
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()