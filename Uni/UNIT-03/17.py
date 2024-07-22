class myclass:
    def sum(self,a=None,b=None,c=None):
        if a != None and b != None and c != None:
            print("Sum of three Numers: ",(a+b+c))
        
        elif a != None and b != None:
            print("Sum of two Numers: ",(a+b))
        
        else:
            print("Please Enter 2 or 3 aruguments")
m=myclass()
m.sum(10,20,30)
m.sum(40,20)
m.sum(100)