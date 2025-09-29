x=1222


if int(x/1000) == x%10:
    if int(x/100)%10 == int(x/10)%10:
        print("yes it is a palindrome")
    else:
        print("No, It is not a palindrome")
else:
    print("no it is not a palindrome")
