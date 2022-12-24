#Once a tuple is created, 
#you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround. You can convert the tuple into a list, change the list, 
#and convert the list back into a tuple.


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orans")
thistuple = tuple(y)
print(thistuple)

# Remove Items
# Note: You cannot remove items in a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

#you can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists








