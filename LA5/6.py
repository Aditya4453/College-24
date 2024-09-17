n=int(input("Enter the number :"))
x=0
y=1

print(y,end=" ")

i=1
while i<(n+1):
    c=x+y #calculation
    print(c,end=" ") #printing fibonnaci of every number
    x=y  #updating the values for further calculations
    y=c
    i=i+1
