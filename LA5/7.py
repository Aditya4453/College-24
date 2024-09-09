n=int(input("Enter the number :"))
i=2
while i<=n/2:
    if n%i==0:
        print(n,"Is Not Prime")
        break
    else :
        if i==n//2:
            print(n,"Is PRIME")
        i=i+1
        
