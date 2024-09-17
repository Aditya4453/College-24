n=int(input("Enter :"))
string=""
while n>0:
    x=n%2
    string=str(x)+string
    n=n//2
print(string)
    
