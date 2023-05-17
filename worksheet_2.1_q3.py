# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged. 
# Example:- Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

string = input("Enter your String: ")

if string.endswith('ing'):
  string += 'ly'
elif len(string) >= 3:
  string += 'ing'

print(string)

# The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.