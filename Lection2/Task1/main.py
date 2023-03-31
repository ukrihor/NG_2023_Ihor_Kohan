# Asking the user to enter the number of elements
n = int(input("Введите количество элементов: "))

# Create an empty list to store items
elements = []

# Asking the user to enter each item and adding it to the list
for i in range(n):
    element = input("Введите элемент: ")
    elements.append(element)

# Asking the user to enter the element to be found
search_element = input("Введите элемент для поиска: ")

# Count the number of occurrences of an element in a list
count = elements.count(search_element)

# Output result
print("Количество элемента", search_element, "в списке:", count)
