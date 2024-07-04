def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            return True
        else:
            return False

list=[1,2,'chirag',4,'Python',6]
n='chirag'
if search(list,n):
    print("Found")
else:
    print("Not Found")