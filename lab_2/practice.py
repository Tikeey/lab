#Example
#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Example
#Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type:

#Example
#String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#A list can contain different data types:

#Example
#A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

#Example
#What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#It is also possible to use the list() constructor when creating a new list.

#Example
#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#ExampleGet your own Python Server
#Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
"""
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
"""
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Example
#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Example
#This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Example
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Example
#Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  #Example
#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Example
#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#ExampleGet your own Python Server
#Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
"""
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert an item as the second position:
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
"""
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
"""
The remove() method removes the specified item.

Example
Remove "banana":
"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
"""
If there are more than one item with the specified value, the remove() method removes the first occurrence:

Example
Remove the first occurrence of "banana":
"""
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Example
#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
"""
If you do not specify the index, the pop() method removes the last item.

Example
Remove the last item:
"""
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
"""
The del keyword also removes the specified index:

Example
Remove the first item:
"""
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
"""
The del keyword can also delete the list completely.

Example
Delete the entire list:
"""
thislist = ["apple", "banana", "cherry"]
del thislist
"""
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:
"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Example
#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

Example
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Example
#Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

#Example
#With no if statement:

newlist = [x for x in fruits]

#Example
#You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

#Example
#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

#Example
#Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

#Example
#Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

#Example
#Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

#Example
#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example
#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Example
#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example
#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Example
#   Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Example
#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Example
#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Example
#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Example
#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
"""
You can also make a copy of a list by using the : (slice) operator.

Example
Make a copy of a list with the : operator:
"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Example
#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Example
#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
"""
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""