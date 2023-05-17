# 3. Write a Python program calculate the product, multiplying all the numbers of a given tuple.


# Define the input tuple
input_tuple = (1, 2, 3, 4, 5)

# Initialize the product to 1
product = 1

# Iterate through the tuple and multiply each number by the current product
for number in input_tuple:
    product *= number

# Print the product of the numbers in the tuple
print("The product of the numbers in the tuple is:", product)
