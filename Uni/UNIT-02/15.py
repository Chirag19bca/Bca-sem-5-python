list1=[i for i in range(1,7)]
list2=[i for i in range(7,11)]
print(list1)
print(list2)
list3=list1+list2
print(list3)
#repetition of list
list=[i for i in list3 for x in (0,1)]
print(list)
#cloning list
list4=list3
print(list4)