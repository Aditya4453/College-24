x=int(input("Enter x:"))
n=int(input("Enter n:"))
sum=1
for i in range(1,n+1):
    p=1
    for j in range(1,i+1):
        p*=j
    sum=sum+(((x)**n)/p)
print(round(sum,9))
