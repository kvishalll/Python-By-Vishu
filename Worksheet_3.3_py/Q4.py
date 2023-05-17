# 4.	Write a Python program to count the frequency of words in a file

# open the file in read mode
with open(r"F:\Py By Vishu\Worksheet_3.3_py\pranav.txt", 'r') as file:
    # read the contents of the file into a string
    contents = file.read()

# split the contents into words
words = contents.split()

# create a dictionary to hold the word frequencies
word_freq = {}

# iterate over the words and update the dictionary
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# print the word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
