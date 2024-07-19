print("\n using class variable")
# using class variable
class sample:
    var=10#class variable
    @classmethod
    def new_modify(cls):
        cls.var+=1
s1=sample()
s2=sample()
print("X in s1: ",s1.var)
print("X in s2: ",s2.var)
s1.new_modify()
print("X in s1: ",s1.var)
print("X in s2: ",s2.var)

#using instance variable
print("\n using instance variable")
class sample:
    def __init__(self):#using this function create instance variable
        self.x=10
    def modify(self):
        self.x+=1
s1=sample()
s2=sample()
print("X in s1: ",s1.x)
print("X in s2: ",s2.x)
s1.modify()
print("X in s1: ",s1.x)
print("X in s2: ",s2.x)
