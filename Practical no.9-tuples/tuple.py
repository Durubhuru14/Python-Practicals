# Creating a tuple of employee records, where each record is a tuple with employee's name, ID, and salary
employees = (
    ("Alice", 101, 50000),
    ("Bob", 102, 60000),
    ("Charlie", 103, 55000),
    ("David", 104, 70000),
    ("Eve", 105, 65000)
)

# Displaying the original tuple of employees
print("Original Employee Records:")
for emp in employees:
    print(f"Name: {emp[0]}, ID: {emp[1]}, Salary: {emp[2]}")

# Example 1: Accessing elements in a tuple
# Accessing the first employee's information
first_employee = employees[0]
print("\nFirst Employee Record:")
print(f"Name: {first_employee[0]}, ID: {first_employee[1]}, Salary: {first_employee[2]}")

# Example 2: Concatenating tuples
new_employees = (
    ("Frank", 106, 71000),
    ("Grace", 107, 72000)
)
updated_employees = employees + new_employees  # Concatenate the original and new employee tuples
print("\nUpdated Employee Records after concatenation:")
for emp in updated_employees:
    print(f"Name: {emp[0]}, ID: {emp[1]}, Salary: {emp[2]}")

# Example 3: Unpacking a tuple
# Unpacking the first employee's tuple into individual variables
name, emp_id, salary = employees[0]
print("\nUnpacking the first employee's record:")
print(f"Name: {name}, ID: {emp_id}, Salary: {salary}")

# Example 4: Finding the length of the tuple
num_of_employees = len(employees)
print(f"\nNumber of employees: {num_of_employees}")

# Example 5: Checking for membership
if ("Bob", 102, 60000) in employees:
    print("\nBob is in the employee records.")
else:
    print("\nBob is not in the employee records.")

# Example 6: Slicing a tuple
# Getting the first three employee records
first_three_employees = employees[:3]
print("\nFirst three employee records:")
for emp in first_three_employees:
    print(f"Name: {emp[0]}, ID: {emp[1]}, Salary: {emp[2]}")
