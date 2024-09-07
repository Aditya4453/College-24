a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
'''print(a,"x**2",+b,"x",+c)'''
D=((b**2)-(4*a*c))
if D<0 :
    print("INVALID CASE")
else:
    x=(-b+((D)**(1/2)))/2*a
    y=(-b-((D)**(1/2)))/2*a
    u=round(x,2)
    v=round(y,2)
    print("the roots of wuadratic equation are :",u,v)
