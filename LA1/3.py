num1= int(input("Enter Length(in ft) :"))
num2= int(input("Enter Width(in ft) :"))

area=num1*num2*0.092903

 

if num1<0 or num2<0 :
    print("Entered Value is invalid")
else:
    print("Area(in sq m) is ",area)
