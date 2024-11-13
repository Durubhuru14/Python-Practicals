# pass_example.py
# This program demonstrates the use of the pass statement in a loop.

# Using pass as a placeholder in a loop
print("Using pass as a placeholder:")
for i in range(1, 5):
    if i == 3:
        pass                 # pass does nothing, used as a placeholder here
    print(f"Processing number: {i}")  # Print each number
