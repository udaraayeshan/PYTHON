'''Python RegEx
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.'''


# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:


#RegEx in Python

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
#   RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# Function	  Description
# findall	 Returns a list containing all matches
# search	 Returns a Match object if there is a match anywhere in the string
# split	     Returns a list where the string has been split at each match
# sub	     Replaces one or many matches with a string



'''Metacharacters
Metacharacters are characters with a special meaning:

Character	     Description	                        Example	
[]	    A set of characters	                              "[a-m]"	
\	    Signals a special sequence 
        (can also be used to escape special characters)	    "\d"	
.	    Any character (except newline character)	     "he..o"	
^	    Starts with	                                    "^hello"	
$	    Ends with	                                     "planet$"	
*	    Zero or more occurrences	                     "he.*o"	
+	    One or more occurrences	                          "he.+o"	
?	    Zero or one occurrences	                          "he.?o"	
{}	    Exactly the specified number of occurrences	     "he.{2}o"	
|	    Either or	                                    "falls|stays"	
()	    Capture and group	 '''


#Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:



#Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:




#The findall() Function

import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)




#The search() Function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 



#The split() Function
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#The sub() Function

# The sub() function replaces the matches with the text of your choice:

# Example
# Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# # Match Object
# Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
