# Ask the user to enter the number of elements
n = int(input("Введите количество элементов: "))

# Create an empty list to store items
elements = []

# Ask the user to enter each element and add it to the list
for i in range(n):
    element = input("Введите элемент: ")
    elements.append(element)

# Ask the user to enter the element to be found
search_element = input("Введите элемент для поиска: ")

# Count the number of occurrences of the element in the list
count = elements.count(search_element)

# Output the result
print("Количество элемента", search_element, "в списке:", count)
