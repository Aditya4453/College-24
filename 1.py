print("Multiplication Table")
print("  |",1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9,sep=" ")
print("------------------------------")
i=1

while i<10:
    a=1
    print(i,"|",end=" ")
    while a<10:
        print(a*i,end=" ")
        a=a+1
    i=i+1
    print("\n")
