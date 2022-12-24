
# Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

                                   #sort()
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#[23, 50, 65, 82, 100]


# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #sort(reverse = True)
print(thislist)



#Customize Sort Function

def myfunc(n):
      return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

