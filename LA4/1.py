salary=int(input("Enter Your Salary:"))
yr_of_service=int(input("Enter no. of years :"))
if yr_of_service>5:
    bonus_amt=0.005*salary
    net_amt=salary+bonus_amt
    print(net_amt)
else:
    print("You are not eligible for bonus")
