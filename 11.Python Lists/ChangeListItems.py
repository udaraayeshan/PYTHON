

# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
