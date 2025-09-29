# tell me whether the given year is a leap year or not.


x= 100

if x%100 == 0:
    if x%400 == 0:
     print("yes")
    else:
        print("no")
else:
    if x%4 == 0:
        print("yes")
    else:
        print("no")
