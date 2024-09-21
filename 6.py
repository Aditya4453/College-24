a=int(input("Enter :"))
L=[]
for i in range (a):
    n=int(input("Enter No :"))
    L.append(n)
p=1
UL=max(L)
r=True
for i in range(UL+1,0,-1):
    for j in L:
        if j%i!=0:
            r=False
            break
        else:
            r=True
    if r==True:
        print("GCD is ",i)
        break
    
