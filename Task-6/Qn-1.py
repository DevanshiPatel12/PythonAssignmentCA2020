""" Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.   """

from math import sqrt
C = 50
H = 30
class calculation:
    def __init__(self, Z):
        self.Z = Z
    def calculate(self):
        Z = self.Z
        for i in Z:
            D = int(i)
            normal = 2*C*D / H
            root = sqrt(normal)
            print("C:{}   D:{}   H:{}   Square Root of [(2*C*D)/H] : {} ".format(C,D,H,root))

c1 = calculation(input("Enter comma separated values : ").split(","))
c2 = c1.calculate()

