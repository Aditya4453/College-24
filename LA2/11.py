n1=int(input("Enter 1st Number :"))
n2=int(input("Enter 2nd Number :"))
n3=int(input("Enter 3rd Number :"))
if n1>n2 and n1>n3 :
    print ("n1 is greater")
elif n2>n1 and n2>n3:
    print("n2 is greater")
else :
    if n3>n1 and n3>n2:
        print ("n3 is greater")
    else :
        print("saare equal")