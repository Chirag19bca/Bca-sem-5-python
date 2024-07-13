def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
               # arr[j],arr[j+1]=arr[j+1],arr[j]
               temp=arr[j]
               arr[j]=arr[j+1]
               arr[j+1]=temp
arr=[64,34,25,12,22,11,90]
print("original array: ")
print(arr)
bubblesort(arr)
print("sortted array: ")
print(arr)