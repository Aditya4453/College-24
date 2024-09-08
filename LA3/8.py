s=float(input("enter the monthly saving amount by user:"))
m=int(input("enter the numbers of months you want to get data of:"))
if s<0 or m<=0:
    print("invalid input")
else:
    i=0.00417
    v=(s*((1+i)**m-1))/i
    print(v)
