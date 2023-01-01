# import mymodule
# mymodule.greeting("Jonathan")


# a = mymodule.person1["age"]
# print(a)





# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Example
# Create an alias for mymodule called mx:

# import mymodule as mx

# a = mx.person1["age"]
# print(a)








# Built-in Modules

import platform

x = platform.system()
print(x)

#Using the dir() Function


import platform

x = dir(platform)
print(x)

#Note: The dir() function can be used on all modules, also the ones you create yourself.



#Import From Module
# You can choose to import only parts from a module, by using the from keyword.


from mymodule import person1

print (person1["age"])


