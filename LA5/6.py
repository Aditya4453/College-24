n=int(input("Enter the number :"))
x=0
y=1

print(y,end=" ")

i=0
while i<(n+1):
    c=x+y
    print(c,end=" ")
    x=y
    y=c
    i=i+1
