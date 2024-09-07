n=int(input("Enter No of Pounds :"))
c=float(input("Enter the amount you deposit :"))
tc=n*2.50
if tc==c :
    print("Transaction Done ! order placed")
elif tc>c:
    s=tc-c
    print("You owe" ,s," more ")
else:
    p=c-tc
    print("You have deposited" ,p," extra")
