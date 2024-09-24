x=int(input("Enter x:"))
n=int(input("Enter n:"))
sum=1
for i in range(1,n+1):
    sum=sum+(((x)**n)/i)
print(round(sum,9))
