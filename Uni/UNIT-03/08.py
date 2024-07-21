class Emp:
    def __init__(self,id,name,sal):#IT is defualt function
        self.id=id
        self.name = name
        self.salary = sal
        
    #Instance Method
    def display(self):
        print("Id: ",self.id)
        print("name: ",self.name)
        print("salary: ",self.salary)
class myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000#Incrementing salary by 1000
        e.display()
e=Emp(3013,"Sadhu Chirag",16000.75)
myclass.mymethod(e)