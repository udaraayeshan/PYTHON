

# What is PIP?

# PIP is a package manager for Python packages, or modules if you like.

# Note: If you have Python version 3.4 or later, PIP is included by default.

# What is a Package?
# A package contains all the files you need for a module.

# Modules are Python code libraries you can include in your project.



#Download a Package

# Download a package named "camelcase":

# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase



#Using a Package

#import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.


# List Packages

# Use the list command to list all the packages installed on your system:

