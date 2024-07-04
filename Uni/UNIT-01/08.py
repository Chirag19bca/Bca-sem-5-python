min=int(input("Enter the minimum no: "))
max=int(input("Enter the maximum no: "))
even_total=0
odd_total=0
for num in range(min,max+1):
    if num%2==0:
        even_total=even_total+num
    else:
        odd_total=odd_total+num
print("the sum of Even Numbers from 1 to {0}: {1}".format(num,even_total))
print("the sum of Odd Numbers from 1 to {0}: {1}".format(num,odd_total))