tup1=("chirag","dhruvil","manan","krish","Akshat","Kiran")
print("Tuple: ",tup1)
li=list(tup1)
li[4]="chess"#if using append() it's take intger values only
tup1=tuple(li)
print("Tuple: ",tup1)