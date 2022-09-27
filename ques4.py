lower_num=int(input("Enter starting number :"))
upper_num=int(input("Enter Ending number :"))
print(f"Prime number between {lower_num} to {upper_num} are :")
for num in range(lower_num,upper_num+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")
                
        