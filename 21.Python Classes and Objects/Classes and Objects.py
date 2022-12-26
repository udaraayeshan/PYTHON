'''Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.'''


# Create a Class
# To create a class, use the keyword class:

# Example
# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5
  
  
#   Create Object
# Now we can use the class named MyClass to create objects:

# Example
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)


#The __init__() Function
# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#The __str__() Function
# The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Object Methods
class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age

 def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#The self Parameter
# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


#Modify Object Properties
# You can modify properties on objects like this:

# Example
# Set the age of p1 to 40:

class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age

def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40
print(p1.age)

#Delete Object Properties
# You can delete properties on objects by using the del keyword:

# Example
# Delete the age property from the p1 object:
#

# Delete Objects
# You can delete objects by using the del keyword:

# Example
# Delete the p1 object:

del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# Example
class Person:
  pass






  