a=int(input("Enter year: "))
if a%4==0 or a%4==100 or a%4==400:
    print(a," is leap year")
else:
    print(a," is not leap year")