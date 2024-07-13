l1=[1,1,2,3,4,3,0,0]
l2=[]
print("list1: ")
print(l1)
for i in l1:
    if i not in l2:
        l2.append(i)
print("list2: ")
print(l2)