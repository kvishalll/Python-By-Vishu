# Python program to check whether the string is Symmetrical or Palindrome
string = input("Enter a string: ")
reverse_string = string[::-1]

# : is a separator that indicates the start and end indices of the slice.
# ::-1 is a step value that tells Python to reverse the string.

if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
if string == string[::-1]:
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")
