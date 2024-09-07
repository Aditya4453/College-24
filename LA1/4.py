x= int(input("Enter Number x :"))
y= int(input("Enter Number y :"))
if x<0 or y<0 :
    print("Invalid Input")
else :
    if y%x==0:
        print("y is divisible by x ")
    else:
        print("y is not divisible by x ")