
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# But we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Example
# Use the format() method to insert numbers into strings:


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))