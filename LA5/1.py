x=int(input("Enter x :"))
y=int(input("Enter y :"))
n=int(input("Enter N :"))
if x<y:
    while x!=y:
        if x%n==0:
            print(x)
            x=x+1
        else:
            x=x+1
        
else:
    while x!=y:
        if y%n==0:
            print(y)
            y=y+1
        else:
            y=y+1
