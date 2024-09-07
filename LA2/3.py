w= int(input("Enter Your Wieght(Kg) :"))
h= int(input("Enter Your Height(m) :"))
B=w/(h**2)
if B<18.5:
    print("they are underweight")
elif B<25 and B>18.5 :
    print("they have a normal weight")
elif B<30 and B>25 :
    print("they are slightly overweight")
elif B<35 and B>30 :
    print("they are obese")
else :
    print("they are clinically obese")

