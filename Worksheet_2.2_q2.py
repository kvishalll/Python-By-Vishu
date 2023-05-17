# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements, Sample List : 
# ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],Expected Output : ['Green', 'White', 'Black']

# Define the original list
original_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Create a new list that excludes the 0th, 4th, and 5th elements
new_list = [original_list[i] for i in range(len(original_list)) if i not in [0, 4, 5]]


print(new_list)