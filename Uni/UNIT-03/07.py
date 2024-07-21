import sys
class bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdrawals(self,amount):
        if amount>self.balance:
            print("Low balance,Cannot withdraw")
        else:
           self.balance-=amount
        return self.balance
#creates an account with given name and balance 0.0
name=input("Enter Bank Name: ")
b=bank(name)
while(True):
    print("\n d/D -Deposit,w/W -Withdrawal,e/E -Exit")
    choice=input("Enter your Choice: ")
    if choice== "e" or choice== "E":
        sys.exit()
    amount=float(input("Enter Amount: "))
    if choice== "d" or choice== "D":
        print("Balance after deposit: ",b.deposit(amount))
    elif choice== "w" or choice== "W":
        print("Balance after withdrawals: ",b.withdrawals(amount))
    