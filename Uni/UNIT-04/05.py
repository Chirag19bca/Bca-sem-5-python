import datetime
year=int(input("Enter your birth year: "))
month=int(input("Enter your birth month: "))
day=int(input("Enter your birth day: "))
brithday=datetime.datetime(year,month,day)
now=datetime.datetime.now()
difference= now - brithday
print("Difference is: ",difference.days,"days")