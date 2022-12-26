'''Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

# Example
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass


#Use the Student class to create an object, and then execute the printname method:

class Person:
 def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#Add the __init__() Function

# Example
# Add the __init__() function to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname):
    #add properties etc.
    
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.



# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
 def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

 def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()


# Add Properties
# Example
# Add a property called graduationyear to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019


# Add Methods
# Example
# Add a method called welcome to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
