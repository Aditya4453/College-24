n=int(input("Enter any number :"))
d=0
nd=0
x=0
while x!=-999:
    x=int(input("Enter any number :"))

    if x%n==0:
        d=d+1
        print("--{x}")
    else:
        nd=nd+1

print(d)
print(nd)          

