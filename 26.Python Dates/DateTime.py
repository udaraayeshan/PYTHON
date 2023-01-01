

'''Python Dates
A date in Python is not a data type of its own, 
but we can import a module named datetime to work with dates as date objects.'''

import datetime

x = datetime.datetime.now()
print(x)


# Date Output

# When we execute the code from the example above the result will be:

# 2023-01-01 22:46:38.936810
# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.

# Here are a few examples, you will learn more about them later in this chapter:


print(x.year)
print(x.strftime("%A"))



#Creating Date Objects

x = datetime.datetime(2020, 5, 17)

print(x)


# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
# but they are optional, and has a default value of 0, (None for timezone).



#The strftime() Method
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
