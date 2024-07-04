choice=0
while(choice!=5):
    print("1. Find area of circle")
    print("2. Find area of triangle")
    print("3. Find area of Square and rectangle")
    print("4. Find Simple Interest")
    print("5. Exit")
    choice=int(input("Enter your Choice: "))
    if choice==1:
        pi=3.14
        r=float(input("Enter the radius of a circle: "))#radius value
        area=pi*r*r
        print("Area of a Circle: ",area)
    elif choice==2:
        a=float(input("Enter First side: "))
        b=float(input("Enter Second side: "))
        c=float(input("Enter Third side: "))
        #calculate the semi-perimeter
        s=(a+b+c)/2
        #calculate the area
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("the area of the triangle: ",area)
    elif choice==3:
        side=int(input("Enter side length of Square: "))
        s_area=side*side#Area of Square
        print("area of Square: ",s_area)
        width=float(input("Enter width of a rectangle: "))
        height=float(input("Enter height of a rectangle: "))
        #calculate area of rectangle
        r_area=width*height
        print("the area of the rectangle: ",r_area)
    elif choice==4:
        p=int(input("Enter P: "))
        r=int(input("Enter R: "))
        n=int(input("Enter N: "))
        i=(p*r*n)/100
        print("Simple Interest: ",i)
    elif choice==5:
        exit()
    else:
        print("Bye Bye")