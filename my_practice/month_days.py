# print how many days are remaining in the given months?


d=0

m1=2



if m1==4 or m1==6 or m1==9 or m1==11:
    print(f"{30-d} days remaining")
elif m1==5 or m1==7 or m1==1 or m1==3 or m1==8 or m1==10 or m1==12:
    print(f"{31-d} days remaining")
elif m1==2:
    print(f"{28-d} days remaining")

else:
    print("na")



