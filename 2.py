n=int(input("Enter the number :"))
i=1
while i<1000 and i>0:
    if i%n==0:
        i+=1
        continue
    print(i)
    i+=1
