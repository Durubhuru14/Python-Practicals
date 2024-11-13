# Create an array (list) in Python
arr = [10, 20, 30, 40, 50, 60]

# Accessing elements using indexing
print("Element at index 0:", arr[0])  # First element: 10
print("Element at index 3:", arr[3])  # Fourth element: 40

# Negative indexing (accessing from the end)
print("Last element:", arr[-1])  # Last element: 60
print("Second last element:", arr[-2])  # Second last element: 50

# Slicing the array (extracting a part of the array)
print("Elements from index 1 to 3:", arr[1:4])  # Slicing: from index 1 to 3 (not including 4)
print("Elements from the beginning to index 3:", arr[:4])  # Slicing: from start to index 3
print("Elements from index 2 to the end:", arr[2:])  # Slicing: from index 2 to the end

# Modifying elements in the array
arr[1] = 25  # Changing the second element (index 1) from 20 to 25
print("Array after modification:", arr)

# Adding elements to the array
arr.append(70)  # Adding a new element at the end of the array
print("Array after appending 70:", arr)

# Inserting an element at a specific position
arr.insert(2, 15)  # Inserting 15 at index 2
print("Array after inserting 15 at index 2:", arr)

# Removing elements from the array
arr.remove(40)  # Removing the element with value 40
print("Array after removing 40:", arr)

# Iterating over the array
print("Iterating over the array:")
for element in arr:
    print(element, end=" ")  # Prints each element in the array

# Using a for loop with index
print("\nIterating over the array using index:")
for i in range(len(arr)):
    print(f"Element at index {i}: {arr[i]}")

# Iterating over array with while loop
print("Iterating over the array using while loop:")
index = 0
while index < len(arr):
    print(arr[index], end=" ")  # Print each element using arr[index]
    index += 1  # Increment the index