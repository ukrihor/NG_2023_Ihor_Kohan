# Asking the user to enter the number of elements
n = int(input("Enter the number of items: "))

# Create an empty list to store items
elements = []

# Asking the user to enter each item and adding it to the list
for i in range(n):
    element = input("Enter element: ")
    elements.append(element)

# Asking the user to enter the element to be found
search_element = input("Enter an item to search: ")

# Count the number of occurrences of an element in a list
count = elements.count(search_element)

# Output result
print("Item Quantity", search_element, "on the list:", count)
