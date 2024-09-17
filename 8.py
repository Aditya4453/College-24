n=int(input("enter the number :"))
for i in range(1,n+1):
    for x in range(n-i,0,-1):
        print(" ",end=" ")
    for y in range(1,2*(i)+1):
        if y%2==0:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
