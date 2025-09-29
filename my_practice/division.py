#  >=60 ist div 45-60 2nd division 33-45 3rd div 28<= final marks pass with grace of 5

x = 63

if x >=60:
    print(" 1st division")
elif x >=45:
    print(" 2nd division")
elif x >= 33:
    print(" 3rd division")

elif x >=28:
    print(f"pass with grace of: {33-x}")
else:
    print(" fail")