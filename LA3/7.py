n=int(input("Enter any number :"))
sum=0
if n>=100 :
    for i in str(n):
        sum=sum+(int(i))**3
    print(sum)
    if sum==n:
        print("this is an Armstrong number")
    else:
        print("This is not an Armstrong number")
else:
    print("enter number of 3digits")
