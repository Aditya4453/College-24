n=int(input("Enter:"))
for i in range(1,n+1):
    for x in range(n-i,0,-1):
        print(" ",end=" ")
    for x in range (1,i+1):
        print("*",end=" ")
    print()
