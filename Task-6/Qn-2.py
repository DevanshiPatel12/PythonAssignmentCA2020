# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape:
    Area = 0
    def Area(self):
       return 0

class Square(Shape):
    def __init__(self, Length):
        self.Length = Length
    def Area(self):
        Area = self.Length * self.Length
        print("Area of Square is : ", Area)

S1 = Square(5)
S1.Area()