n=int(input("Enter the number :"))
r=0
for i in range(1,n+1):
    if i%2!=0:
        r=r+(1/((i)**2))
    else:
        r=r-(1/((i)**2))
print(round(r,9))
