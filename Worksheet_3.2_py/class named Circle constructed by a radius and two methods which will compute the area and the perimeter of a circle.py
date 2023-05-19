# 4.	Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def compute_area(self):
        area = 3.14 * (self.radius ** 2)
        return area
    
    def compute_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter
# create an instance of the Circle class
circle = Circle(5)

# compute the area and perimeter of the circle
area = circle.compute_area()
perimeter = circle.compute_perimeter()

# display the area and perimeter of the circle
print(area)
print(perimeter)
