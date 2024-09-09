sent=input("Enter The Sentence :")
i=0
cap,small,dig,sp_char=0,0,0,0
while i<len(sent):
    if sent[i]>='A' and sent[i]<='Z':
        cap=cap+1
    elif ord(sent[i])>= 97 and ord(sent[i])<=122:
        small=small+1
    elif ord(sent[i])>= 48 and ord(sent[i])<=57:
        dig=dig+1
    else:
        sp_char=sp_char+1
    i=i+1

print("Capital Charactars :",cap)
print("Small Letters :",small)
print("Number of Digits :",dig)
print("Special Char :",sp_char)
