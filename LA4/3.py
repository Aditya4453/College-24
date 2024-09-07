shape=input("Enter Shape:")
if shape=="Square":
    s=float(input("Enter side :"))
    area=s*s
    print("Area of square :",round(area,3))
elif shape=="rectangle":
    l=float(input("Enter length :"))
    b=float(input("Enter breadth :"))
    area=l*b
    print("Area of rectangle :",round(area,3))
elif shape=="circle":
    r=float(input("Enter radius :"))
    area=2*3.14*r
    print("Area of circle :",round(area,3))
else:
    base=float(input("Enter base :"))
    altitude=float(input("Enter altitude :"))
    area=0.5*base*altitude
    print("Area of triangle :",round(area,3))
