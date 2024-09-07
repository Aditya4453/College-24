c=input("Enter color of sky :")
m=input("Enter mode:")
w=m+c
print(w)
if w=="SteadyBlue":
    print("clear view")
elif w=="FlashingBlue":
    print("Clouds due")
elif w=="SteadyRed":
    print("Rain Ahead")
else:
    print("Snow instead")
