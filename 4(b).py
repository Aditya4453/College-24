n=int(input("Enter:"))
for i in range(1,n+1):
    for x in range(n-i,0,-1):
        print(" ",end=" ")
    for x in range (65,65+(2*i)-1):
        print(chr(x),end=" ")
    for x in range(n-i,0,-1):
        print(" ",end=" ")
    print()
    
