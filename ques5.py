n=int(input("Enter number :"))
a=n+1
while True:
    if a>1:     
        for i in range(2,int(a/2)+1):
            if a%i==0:
                break
        else:
            print(n," next prime number is :",a)
            break
    a+=1
    
        
        
        