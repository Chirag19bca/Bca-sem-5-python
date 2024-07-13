import array as arr
a=arr.array('i',[1,2,3,4,5])
#display array
print(a)
#update array using indexing
a[0]=7
print(a)
#update array using slicing (a[0:10] 0 is start point,10 is end point)
a[0:3]=arr.array('i',[8,9,16])
print(a)