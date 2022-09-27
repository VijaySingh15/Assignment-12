n=int(input("Enter number :"))
reverse=0
while n>0:
    a=n%10
    reverse=reverse*10 + a
    n//=10
print("Reverse Number :",reverse)
    
    