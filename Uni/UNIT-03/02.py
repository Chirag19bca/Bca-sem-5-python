class student:
    def __init__(self,nm='.',ag=19,m=13):#default funcation in class
        self.name=nm
        self.age=ag
        self.marks=m
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Mark: ",self.marks)

s=student("Chirag",20,96)
s.display()
s1=student("Akshat")
s1.display()