n=int(input("Enter any number :"))
sum=0
if n>=100 :
    for i in str(n):
        sum=sum+int(i)
    print(sum)
else:
    print("enter number of 3digits")

if sum%3==0:
    print("Sum of digits is divisible by 3")
else :
    print("Sum of digits is not divisible by 3")
