# adding, replacing and removing item s in a list.

# we can add item with append, insert and extend.
#append always add item end to the list.
# insert always used ti insert items to the list.
# extend is used to add two list together.


fruits = ['apple', 'banana', 'orange']
fruits.extend(["strawberry", "mangoes" , "blueberries"])
print(fruits)

# we can remove item by using clear, pop, remove.
fruits.pop() #( pop is used to remove last item from the list.
print(fruits)

fruits.remove("orange")
print(fruits) # remove is used to remove specific item from the list.

#fruits.clear() # clear is used to remove every itm from the list.
#print(fruits)

print(fruits)

#  we can replace item in the list by using list indexing.
fruits[2]= "blueberries"
print(fruits)
# use [::-1] to reverse the whole list from last to start.
