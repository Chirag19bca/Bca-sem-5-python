list=[1,2,3,3,3,3,4,5,6,7]
list.append(9)
list.insert(3,20)
print(list)
list.remove(20)
print(list)
list.pop()
print(list)
print(list.index(3))
print(list.count(3))
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.tolist())