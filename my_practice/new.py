# palindrome - number same from left and right
# 11,121,3443,34543

# make 3 digit palindrome

x= 4334

if int(x/1000) == int(x%10):
    if int(int(x/10)%10) == int(int(x/100)%10):
        print("yes it is a palindrome")
    else:
        print("no it is not a palindrome")
else:
    print( "no it is not a palindrome")

