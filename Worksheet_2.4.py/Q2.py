# 2. Write a Python program to remove an empty tuple(s) from a list of tuples


tuples_list = [(1, 2, 3), (), (4, 5), (), (6,), (), ()]

# Iterate through the list of tuples and remove any empty tuples
for t in tuples_list:
    if not t:
        tuples_list.remove(t)

# Print the updated list of tuples
print(tuples_list)