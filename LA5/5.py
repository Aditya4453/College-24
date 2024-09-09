n=int(input("Enter any number:"))
p=0
s=""
if n>9999:
    for i in str(n):
        s=s+i
        p=int(s)
    print(p)
    if p==n :
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")
else:
    print("enter number with 5 digits or more")
