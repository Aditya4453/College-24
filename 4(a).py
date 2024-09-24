n=int(input("Enter number of lines :"))
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for j in range(65,(65+i)):
        print(chr(j),end=" ")
    print()
