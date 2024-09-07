p1x=int(input("Enter point 1 x of triangle:"))
p1y=int(input("Enter point 1 y of triangle:"))
p2x=int(input("Enter point 2 x of triangle:"))
p2y=int(input("Enter point 2 y of triangle:"))
p3x=int(input("Enter point 3 x of triangle:"))
p3y=int(input("Enter point 3 y of triangle:"))

s1=((p2x-p1x)**2+(p2y-p1y)**2)**(1/2)
s2=((p3x-p1x)**2+(p3y-p1y)**2)**(1/2)
s3=((p3x-p2x)**2+(p3y-p2y)**2)**(1/2)

s=(s1+s2+s3)/2
area=((s)*(s-s1)*(s-s2)*(s-s3))**(1/2)

print(p1x,p1y)
print(p2x,p2y)
print(p3x,p3y)
print(area)
