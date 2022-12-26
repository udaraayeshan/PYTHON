'''Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
# Looping Through a String
for x in "banana":
      print(x)
      
#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
      
      
# The continue Statement
    fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
#The range() Function
for x in range(6):
      print(x)
          
for x in range(2, 6):
      print(x)
      
for x in range(2, 30, 3):
      print(x)
      
      #Else in For Loop
for x in range(6):
      print(x)
else:
  print("Finally finished!")
  
  
  #Nested Loops
  
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    
    
    #Nested Loops
    
  #for x in [0, 1, 2]:
  pass
      

      


  
  