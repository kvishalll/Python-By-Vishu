# Write a  program to enter length in centimeter and convert it into meter and kilometer,
# and also convert the same into Equivalents

cm = int(input("Enter the value of cm: "))

meter = cm / 100.0
kilometer = cm / 100000.0

print("Length in meter = " ,meter , "m")
print("Length in Kilometer = ",kilometer , "km")
