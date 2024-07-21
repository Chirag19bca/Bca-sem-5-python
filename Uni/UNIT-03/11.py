class teacher:
    def __init__(self):#IT is defualt function
        self.id = 1001
        
    #Instance Method
    def display(self):
        print("Teachers id: ",self.id)

class student(teacher):
    def __init__(self):
        self.id=1
        
    def display(self):
        print("Students Id: ",self.id)

s=student()
s.display()