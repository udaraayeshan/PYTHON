# Python Functions

# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


# Creating a Function
# In Python a function is defined using the def keyword:

# Example
def my_function():
  print("Hello from a function")
  
#Calling a Function
my_function()

#Arguments

def my_function(fname):

 print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arbitrary Arguments, *args

def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Keyword Arguments

def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
      print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Default Parameter Value
def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
      for x in food:
       print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values


def my_function(x):
      return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#The pass Statement
def myfunction():
      pass

