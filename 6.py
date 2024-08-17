r= int(input("Enter Radius  :"))
if r>0 and r<100 :
    area=3.14*(r**2)
    print("The area of circle :",area)
else:
    print("Sorry!I cant take value other than 0 to 100")