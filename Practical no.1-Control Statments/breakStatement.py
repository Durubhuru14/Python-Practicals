# break_example.py
# This program demonstrates the use of the break statement in a loop.

# Using a for loop with break to exit the loop when i is 5
print("Using break to stop the loop when the value reaches 5:")
for i in range(1, 10):
    if i == 5:
        print("Break at 5")  # Display a message when the loop breaks
        break                # Exit the loop when i equals 5
    print(i, end=" ")        # Print the current value of i
print()  # Print a newline at the end
