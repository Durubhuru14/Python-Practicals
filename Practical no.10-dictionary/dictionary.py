# Creating a dictionary of students with their grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "David": 75,
    "Eve": 90
}

# Displaying the original dictionary
print("Original Student Information:")
print(students)

# Example 1: Adding a new student and their grade
students["Frank"] = 95  # Adds a new student with grade 95
print("\nAfter adding Frank:")
print(students)

# Example 2: Updating an existing student's grade
students["Alice"] = 89  # Updates Alice's grade to 89
print("\nAfter updating Alice's grade:")
print(students)

# Example 3: Removing a student from the dictionary
del students["David"]  # Removes David from the dictionary
print("\nAfter removing David:")
print(students)

# Example 4: Checking if a student is in the dictionary
if "Eve" in students:
    print("\nEve is in the dictionary.")
else:
    print("\nEve is not in the dictionary.")

# Example 5: Iterating over the dictionary using keys
print("\nIterating over the dictionary using keys:")
for student in students:
    print(f"Student: {student}")

# Example 6: Iterating over the dictionary using values
print("\nIterating over the dictionary using values:")
for grade in students.values():
    print(f"Grade: {grade}")

# Example 7: Iterating over the dictionary using keys and values
print("\nIterating over the dictionary using keys and values:")
for student, grade in students.items():
    print(f"{student}: {grade}")

# Example 8: Getting the number of students in the dictionary
num_students = len(students)
print(f"\nTotal number of students: {num_students}")

# Example 9: Getting a student's grade using the get() method
grade = students.get("Bob", "Not Found")  # Returns 'Not Found' if Bob is not in the dictionary
print(f"\nBob's grade: {grade}")

# Example 10: Using popitem() to remove and return the last inserted item
last_item = students.popitem()  # Removes and returns the last inserted item
print(f"\nRemoved last item using popitem(): {last_item}")
print("Updated dictionary after popitem():")
print(students)

# Example 11: Using clear() to remove all items from the dictionary
students.clear()  # Clears all items from the dictionary
print("\nDictionary after clear() - All items removed:")
print(students)

# Recreating the dictionary for further operations
students = {
    "Alice": 89,
    "Bob": 92,
    "Charlie": 88,
    "Eve": 90,
    "Frank": 95
}

# Example 12: Merging two dictionaries
new_students = {
    "Grace": 93,
    "Hannah": 80
}
students.update(new_students)  # Merges the new_students dictionary into the existing one
print("\nAfter merging new students:")
print(students)

# Example 13: Copying the dictionary using copy()
students_copy = students.copy()  # Creates a shallow copy of the dictionary
print("\nOriginal Dictionary:")
print(students)
print("\nCopied Dictionary:")
print(students_copy)

# Demonstrating that the copied dictionary is a separate object
students_copy["Grace"] = 96  # Modifying the copy
print("\nAfter modifying copied dictionary:")
print(f"Original Dictionary: {students}")
print(f"Copied Dictionary: {students_copy}")