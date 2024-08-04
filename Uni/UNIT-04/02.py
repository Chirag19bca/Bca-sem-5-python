try:
    a=eval(input("Enter a dividend: "))
    b=eval(input("Enter a divisor: "))
    ans=a/b
    
except (TypeError,SyntaxError):
    print("Error")

else:
    print("ans: ",ans)