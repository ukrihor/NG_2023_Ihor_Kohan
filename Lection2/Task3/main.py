# we ask the user for three sets of elements
set1 = set(input("Enter the elements for the first set separated by spaces: ").split())
set2 = set(input("Enter the elements for the second set separated by spaces: ").split())
set3 = set(input("Enter elements for the third set separated by spaces: ").split())

# find the intersection of sets and remove duplicates
non_unique_elements = set1.intersection(set2, set3)

# Output result
print("Set of non-unique elements: ", *non_unique_elements)
