# Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line
import string

# define the number of letters per line
letters_per_line = 5

# create a string of all uppercase letters
alphabet = string.ascii_uppercase

# open a new file for writing
with open('alphabet.txt', 'w') as file:
    # iterate over the alphabet and write each letter to the file
    for i in range(0, len(alphabet), letters_per_line):
        line = alphabet[i:i+letters_per_line]
        file.write(line + '\n')
