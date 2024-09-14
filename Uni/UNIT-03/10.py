class square:
    def __init__(self,x):#IT is defualt function
        self.x=x
    def area(self):
        print("Area of Square: ",self.x * self.x)
class rectangle(square):
    def __init__(self,x,y):#IT is defualt function
        super().__init__(x)
        self.y=y
    def area(self):
        super().area()
        print("Area of rectangle: ",self.x * self.y)
a,b=[float(x) for x in input("Enter length and breadth: ").split()]
r=rectangle(a,b)
r.area()
