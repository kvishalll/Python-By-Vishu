# 4.	Write a Python program to convert a tuple of string values to a tuple of integer values.


# Define the input tuple of string values
string_tuple = ('10', '20', '30', '40', '50')

# Use a list comprehension to convert each string value to an integer value
int_list = [int(s) for s in string_tuple]

# Convert the list of integers to a tuple
int_tuple = tuple(int_list)

# Print the original and converted tuples
print("Original tuple of string values:", string_tuple)
print("Tuple of integer values:", int_tuple)
