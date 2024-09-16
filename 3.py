n=int(input("enter the number :"))
i=1 
while i<=n:
    j=1
    while j<=1:
        print("*",end="")
        j=j+1
    i=i+1
n=int(input("Enter the no. of lines :"))
for i in range (1,n+1):
    N=1
    for N in range(1,i+1):
        print("*",end=" ")
    print("\n")
