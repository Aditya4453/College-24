n=int(input("Enter the number :"))
sum=0
for i in range(1,n+1):
    p=1
    for j in range(1,i+1):
        p*=j
    sum+=(1/p)
print(round(sum,9))
