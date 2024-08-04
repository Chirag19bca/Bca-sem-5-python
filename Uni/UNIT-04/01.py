a=int(input("Enter a dividend: "))
b=int(input("Enter a divisor: "))
try:
    ans=a/b
    
except ZeroDivisionError:
    print("Zero division error")

else:
    print("Answer: ",ans)