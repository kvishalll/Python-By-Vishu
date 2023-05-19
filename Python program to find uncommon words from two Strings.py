# Python program to find uncommon words from two Strings
str1 = input('Enter first string : ')
str2 = input('Enter second string : ')

# finding uncommon words
count = {}
for word in str1.split():
    count[word] = count.get(word, 0) + 1
for word in str2.split():
    count[word] = count.get(word, 0) + 1
  
uncommonWords =  [word for word in count if count[word] == 1]

# printing uncommon words 
print("All uncommon words from both the string are ", uncommonWords)
