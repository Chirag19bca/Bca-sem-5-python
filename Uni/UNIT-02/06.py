def prime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(a," is not prime number")
                break
        else:
            print(a," is prime number")
    else:
            print(a," is not prime number")
a=int(input("Enter Number to check prime or not: "))
prime(a)