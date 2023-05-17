''' Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300},d2 = {'a': 300, 'b': 200, 'd':400}

'''
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# create a new dictionary
result = {}

# iterate through the keys of d1 and d2
for key in d1.keys() | d2.keys():
    # add the values for common keys
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print(result)

''' In this example, the | operator is used to get a set of all the keys in both dictionaries.
The get() method is used to retrieve the value of a key if it exists in the dictionary,
or a default value of 0 if it does not exist. The result dictionary is then populated with the sum of the values for each key.

'''
