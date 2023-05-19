# 5.Write a Python program to check if a specified element presents in a tuple of tuples

# Define the input tuple of tuples
input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Define the element to search for
search_element = 5

# Use a nested loop to iterate through each element in each tuple and check if it matches the search element
found = False
for tuple_elem in input_tuple:
    for elem in tuple_elem:
        if elem == search_element:
            found = True
            break
    if found:
        break

# Print whether the element was found or not
if found:
    print("The element", search_element, "was found in the input tuple of tuples.")
else:
    print("The element", search_element, "was not found in the input tuple of tuples.")
