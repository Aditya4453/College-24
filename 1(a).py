import math
n=360
print("Deg. ","Sin    ","Cos",sep=" ")
for i in range(0,n+1,10):
    print(i ,round(math.sin(i),4),round(math.cos(i),4),sep="   ")
