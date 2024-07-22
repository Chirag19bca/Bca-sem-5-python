class dog:
    def bark(self):
        print("Bow Wow")
class duck:
    def talk(self):
        print("Quack Quack")
class human:
    def talk(self):
        print("Hello,Hi")
#this method accepts an object and calls talk() method
def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    else:
        print("wrong object password")
x=duck()
call_talk(x)
x=human()
call_talk(x)
x=dog()
call_talk(x)