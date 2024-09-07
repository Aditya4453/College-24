hol=int(input("Enter the number of holidays :"))
wrk_days=365-hol
play_hol=hol*127
play_wrk=wrk_days*63
total_ply_min=play_hol+play_wrk
total_min=365*24*60
diff=total_min-total_ply_min
if diff<30000:
    print("Tom cant sleep well")
else :
    print("tom can sleep well")
