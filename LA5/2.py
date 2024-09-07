n=int(input("Enter any number :"))
sum=0
if n>0:
    while n!=0:
       x=n%10
       sum=sum+x
       n=n//10
else:
    print("print any positive number please !!")
    
print(sum)
