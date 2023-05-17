# 3.	Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def compute_area(self):
        area = self.length * self.width
        return area
# create an instance of the Rectangle class
rect = Rectangle(5, 10)

# compute the area of the rectangle
area = rect.compute_area()

# display the area of the rectangle
print(area)