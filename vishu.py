# Write a Python program to read a random line from a file.

import random

# open the file in read mode
with open(r"Yaha kar dena paste", 'r') as file:
    # read all the lines into a list
    lines = file.readlines()

# choose a random line from the list
random_line = random.choice(lines)

# print the random line
print(random_line)

# this is comments