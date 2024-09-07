s1=int(input("enter side :"))
s2=int(input("enter side :"))
s3=int(input("enter side :"))

s=(s1+s2+s3)/2
area=((s)*(s-s1)*(s-s2)*(s-s3))**(1/2)

if s1<0 or s2<0 or s3<0 :
    print("Please enter positive number ")
else :
    print(area)
    print("they can form triangle")
