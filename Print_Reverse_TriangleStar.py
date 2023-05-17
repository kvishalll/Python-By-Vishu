# Print reverse triangle star in python
n = int(input("Enter the value of n: "))

for i in range(0,n):

    for j in range(i+1, n):
        print("* ", end="")

    print()