# 1. ask a user for their age and how long they have had their subscription for in years.

age  = input("how old are you")
subscription_length = input( " how long do u have subscription with us")

# use qualify for the discount if they meet the following criteria.
# the user is a student (under 25 year old) or senior citizen (65 year old or older)
# the user has had their subscription length for at least 12 months.

# 2. print out the following message if the user does qualify for the discount.

# great news you rae qualify

# print if they don not

# sorry better luck next time.

if (int(age) < 25 or int(age )>65) and int(subscription_length) >1:
    print("great news you are qualified")
else:
    print("sorry better luck next time")



