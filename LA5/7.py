n=int(input("Enter the number :"))
if n==2 or n==3: # Checking for number 2 and 3 and for other loop is working
    print(n,"Is Prime")
i=2
while i<=n/2:
    if n%i==0:
        print(n,"Is Not Prime")
        break
    else :
        if i==n//2:
            print(n,"Is PRIME")
        i=i+1
        
