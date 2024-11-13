# continue_example.py
# This program demonstrates the use of the continue statement in a loop.

# Using a for loop with continue to skip even numbers
print("Using continue to skip even numbers:")
for i in range(1, 10):
    if i % 2 == 0:
        continue             # Skip the rest of the loop if i is even
    print(i, end=" ")        # Print only odd numbers
print()  # Print a newline at the end
