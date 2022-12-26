'''
Python Arrays
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Arrays
Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.'''

# eg
cars = ["Ford", "Volvo", "BMW"]

print(cars)

# Access the Elements of an Array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]

#Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"

# The Length of an Array
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)

#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)
  
#   Adding Array Elements
# You can use the append() method to add an element to an array.

# Example
# Add one more element to the cars array:

cars.append("Honda")


# emoving Array Elements
# You can use the pop() method to remove an element from the array.

# Example
# Delete the second element of the cars array:

cars.pop(1)

# You can also use the remove() method to remove an element from the array.

# Example
# Delete the element that has the value "Volvo":

cars.remove("Volvo")

# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list






