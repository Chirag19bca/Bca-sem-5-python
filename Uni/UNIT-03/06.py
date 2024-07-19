class myclass:
    n=0
    def __init__(self):
        myclass.n+=1
        
    #Static Method
    def no_of_objects():
        print("No Of instance created are",myclass.n)
        
obj1 = myclass()
obj2 = myclass()
obj3 = myclass()
obj4 = myclass()
obj5 = myclass()
myclass.no_of_objects()