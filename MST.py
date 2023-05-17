# calculate the cube of odd no. only and square of even no only
def Cube_And_sq_of_no():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Square of", num, "is", num**2)
        print("Number is even")
    else:
        print("Cube of", num, "is", num**3)
        print("Number is odd")

Cube_And_sq_of_no()