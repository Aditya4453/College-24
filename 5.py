a=int(input("Enter :"))
L=[]
for i in range (a):
    n=int(input("Enter No :"))
    L.append(n)
LL=max(L)
p=1
for i in L:
    p=p*i
UL=p
r=True
for i in range(LL,UL+1):
    for j in L:
        if i%j!=0:
            r=False
            break
        else:
            r=True
    if r==True:
        print("LCM is ",i)
        break
