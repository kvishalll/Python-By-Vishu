# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

my_dict = {'a': 300, 'b': 100, 'c': 500, 'd': 200, 'e': 600, 'f': 400}

# get the keys with the highest 3 values
highest_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

# get the corresponding highest values
highest_values = [my_dict[key] for key in highest_keys]

print("Highest 3 values in the dictionary:")
for i in range(len(highest_keys)):
    print(f"{highest_keys[i]}: {highest_values[i]}")

'''In this example, the sorted() function is used to sort the keys of the dictionary by their values, in descending order. 
The key argument specifies that the sorting should be based on the values of the dictionary, rather than the keys. 
The reverse=True argument sorts the keys in descending order. The [:3] slice gets the first 3 keys in the sorted list.
The highest_values list comprehension gets the corresponding values for the highest keys by iterating through the highest_keys list and getting the value for each key from the dictionary.'''