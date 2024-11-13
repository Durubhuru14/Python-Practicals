# Program to conclude if the given integer `n` is positive or negative using Conditional Statments (if..elif..else)
n = int(input("Enter an integer: "))

if(n > 0):
    print(f"The given integer `{n}` is a positive")
elif(n < 0):
    print(f"The given integer `{n}` is a negative")
else:
    print(f"The given integer zero({n}) is neither negative or positive")