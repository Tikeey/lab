"""
Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

#Example
x = 5
y = "John"
print(x)
print(y)
"""
Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
"""
Get the Type
You can get the data type of a variable with the type() function.

Example
"""
x = 5
y = "John"
print(type(x))
print(type(y))
"""
Single or Double Quotes?
String variables can be declared either by using single or double quotes:

Example
"""
x = "John"
# is the same as
x = 'John'
"""
Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:
"""
a = 4
A = "Sally"
#A will not overwrite a
"""
Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

ExampleGet your own Python Server
x, y, z = "Orange", "Banana", "Cherry"
"""
print(x)
print(y)
print(z)
"""
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

Example
Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
"""
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:

#Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#You can also use the + operator to output multiple variables:

#Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

ExampleGet your own Python Server
Create a variable outside of a function, and use it inside the function
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

#Example
#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

#Example
#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Also, use the global keyword if you want to change a global variable inside a function.

#Example
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

