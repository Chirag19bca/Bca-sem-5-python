import math
class square:
    def area(self,x):
        print("Area of square: ",(x*x))

class circle(square):
    def area(self,x):
        print("Area of circle:%.2f "%(math.pi*x*x))

c=circle()
c.area(4)