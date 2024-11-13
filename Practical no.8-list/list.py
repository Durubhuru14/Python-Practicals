# Creating a list of shopping items
shopping_list = ["Apples", "Bananas", "Carrots", "Milk", "Bread"]

# Displaying the original shopping list
print("Original Shopping List:")
print(shopping_list)

# Example 1: Adding an item to the list
shopping_list.append("Eggs")  # Adds "Eggs" at the end of the list
print("\nAfter adding 'Eggs' to the list:")
print(shopping_list)

# Example 2: Updating an item in the list
shopping_list[1] = "Oranges"  # Replaces "Bananas" with "Oranges"
print("\nAfter updating 'Bananas' to 'Oranges':")
print(shopping_list)

# Example 3: Removing an item from the list by value
shopping_list.remove("Milk")  # Removes the first occurrence of "Milk"
print("\nAfter removing 'Milk' from the list:")
print(shopping_list)

# Example 4: Removing an item from the list by index
del shopping_list[3]  # Removes the item at index 3 (i.e., "Bread")
print("\nAfter removing item at index 3 (Bread):")
print(shopping_list)

# Example 5: Iterating over the list using a for loop
print("\nIterating over the shopping list:")
for item in shopping_list:
    print(item)

# Example 6: Checking if an item exists in the list
if "Eggs" in shopping_list:
    print("\n'Eggs' is in the shopping list!")
else:
    print("\n'Eggs' is not in the shopping list.")

# Example 7: Sorting the list alphabetically
shopping_list.sort()
print("\nAfter sorting the shopping list:")
print(shopping_list)

# Example 8: Reversing the list
shopping_list.reverse()
print("\nAfter reversing the shopping list:")
print(shopping_list)