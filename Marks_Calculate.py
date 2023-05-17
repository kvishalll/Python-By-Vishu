# Write a  program to enter marks of five subjects and calculate total, average and percentage.

a = int(input("Enter the first marks: "))
b = int(input("Enter the second marks: "))
c = int(input("Enter the 3rd marks: "))
d = int(input("Enter the 4th marks: "))
e = int(input("Enter the 5th marks: "))


Total = a+b+c+d+e
average = Total / 5
percentage = (Total / 500)*100 

print("Total marks is: ", Total)
print("Total average is: ", average)
print("Total percentage is: ", percentage)