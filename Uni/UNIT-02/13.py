import employee
print("SALARY PROGRAM")
name=str(input("Enter name of employee: "))
basic=float(input("Enter basic salary: "))
netpay=employee.netpay(basic)
print("net salary: ",netpay)
grosspay=employee.gross(basic,netpay)
print("Gross salary: ",grosspay)