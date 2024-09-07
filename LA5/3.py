n=int(input("Enter any number :"))
l=[]
d=[]
nd=[]
sum_of_divisible=0
sum_of_not_divisible=0
x=int(input("Enter any number :"))

while x!=-999:
    l.append(x)
    x=int(input("Enter any number :"))
for i in l:
    if i%n==0:
        d.append(i)
    else:
        nd.append(i)
        
for i in d:
    sum_of_divisible=sum_of_divisible+i
    
    
for i in nd:
    sum_of_not_divisible=sum_of_not_divisible+i
    
               
print("Summ of all divisible number :",sum_of_divisible)
print("Summ of all not divisible number :",sum_of_not_divisible)
