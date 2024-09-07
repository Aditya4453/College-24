x=int(input("Enter your salary(in LPA) :"))
if x<3:
    print ("0% Income Tax")
elif x>=3 and x<10 :
    print("10% of the gross salary")
elif x>=10 and x<25:
    print("20% of the gross salary")
else:
    print("30% of the gross salary")    