B=int(input("Budget: "))
S=input("Season (Winter/Summer): ").capitalize()
if B>1000:
    print("Vacation place: somewhere in Europe")
    print(B*0.9,"will be spent in stay.")
if B<=100:
    print("Vacation place: somewhere in Bulgaria")
    if S=='Winter':
        print(B*0.3, "will be spent in stay.")
    if S=='Summer':
        print(B*0.7, "will be spent in stay.")
if B<=1000:
    print("Vacation place: somewhere in Balkans")
    if S=='Winter':
        print(B*0.4, "will be spent in stay.")
    if S=='Summer':
        print(B*0.8, "will be spent in stay.")
