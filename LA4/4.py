hours=int(input("Enter hour :"))
mi=int(input("Enter minutes:"))
if hours>23:
    print("Bye Bye")
else:
    print("Time right now :",hours,":",mi)
    aft_tm=mi+15
    if aft_tm>59:
        hours=hours+1
        mi=aft_tm-60
        if mi<10:
            print("Time after 15 min :",hours,":","0",mi)
        else:
            print("Time after 15 min :",hours,":",mi)
    else:
        print("Time after 15 min :",hours,":",aft_tm)
    
