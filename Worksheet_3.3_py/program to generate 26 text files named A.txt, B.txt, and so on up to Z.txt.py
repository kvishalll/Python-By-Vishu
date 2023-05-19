# 1.	Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

# create a string of all uppercase letters
letters = string.ascii_uppercase

# iterate over the letters and create the files
for letter in letters:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        pass
