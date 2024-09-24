n=int(input("Enter :"))
for i in range(1,n+1):
    if i==1 or i==n:
        for i in range(n):
            print("*",end=" ")
    else:
        s=n//2
        print("*",end=" ")
        for j in range(s-i):
            print(" ",end=" ")
        print("*",end=" ")
        for j in range(s,0,-1):
            print(" ",end=" ")
    print()
