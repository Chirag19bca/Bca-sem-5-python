class student:
    def __init__(self):#IT is defualt function
        self.name="sachin"
        self.age = 23
        self.mark = 79
        
    #Instance Method
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Mark: ",self.mark)

s=student()
s.display()