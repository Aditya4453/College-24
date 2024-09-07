dist=int(input("Enter no of kilometers :"))
per=input("Enter period of the day(day or night):")
taxd_prce=37.89*dist
taxn_prce=43.17*dist
busd_prce=4.32*dist
train_prce=2.88*dist
if per=="day":
    if dist<21:
        if taxd_prce<busd_prce and taxd_prce<train_prce:
            print(taxd_prce)
        elif busd_prce<taxd_prce and busd_prce<train_prce:
            print(busd_prce)
        else:
            print(train_prce)
    elif dist>20 and dist<101:
        if taxd_prce>train_prce:
            print("train :",train_prce)
        else:
            print("taxi :",taxd_prce)
    else:
        print("Taxi is the only option :",taxd_prce)
else:
    if dist<21:
        if taxn_prce<busd_prce and taxn_prce<train_prce:
            print(taxn_prce)
        elif busd_prce<taxn_prce and busd_prce<train_prce:
            print(busd_prce)
        else:
            print(train_prce)
    elif dist>20 and dist<101:
        if taxn_prce>train_prce:
            print("train :",train_prce)
        else:
            print("taxi :",taxn_prce)
    else:
        print("Taxi is the only option :",taxn_prce)
