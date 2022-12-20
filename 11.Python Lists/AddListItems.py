

# Add List Items
#To add an item to the end of the list, use the append() method:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#Extend List
#To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
