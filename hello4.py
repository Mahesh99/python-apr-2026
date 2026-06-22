print("Welcome to python programming classes")
print("Hello world")
print(323423424+400000)
print("3+4")
print(3-4)
print(3*4)
print(4/2)
print(6%2)
print(5%2)
print(5/2)
print(5//2)
print(6//2)
print(5**2)
print(2**3)

# print(3**4)
#Arithmetic operators (+,-,*,/,%,//,**)
# % modulus
# // floor division
# ** exponentiation

"""
print(5//2)
print(6//2)
print(5**2)
print(2**3)
"""

# Variables
a=10
b=20
c=a+b
print(c)

today_temp=35
mt_everest_ht=8999
print(today_temp+2)
"""
ht
2a
del
and2
_i_
temp
"""

# assignment
# =
x=10
x*=5 # x=x+5 
print(x)

# there are 4 types of basic data types in python
# int,float,bool,str
a=10 # int -23423,21341244243
b=1.1 # float -1.3
c=True # bool False
d="hello" # str "10","python",'hi'





# type() - it is an inbuilt function which is used to find the type of a variable or value
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(10))
print(type(1.1))
print(type(True))
print(type("hello"))



# Type conversion
# int(),float(),str(),bool()
print(int(1.1)) 
print(int("10"))
print(int(10))
print(int(True))
print(int(False))

print(float(10))
print(float("10"))
print(float(1.1))
print(float(True))
print(float(False))

print(str(10))
print(str(1.1))
print(str(True))
print(str(False))
# str(10)
# str(1.1)
# str(True)
# str(False)

print(bool(10))
print(bool(1.1))
print(bool("hello"))
print(bool(""))


# comparison operators
"""
>	 	 	 	 greater than
<          less than
>=  	 	 	   greater than or equal to
<=         less than or equal to
==          equal to
!=          not equal to
"""
print()
print(10>5.1) # True
print(10<5) # False
print(10>=5) # True
print(10<=5) # False
print(10==5) # False
print(10!=5) # True

a=10>5
b=10<5
print(type(a),a)
print(type(b),b)


# logical operators
# and,or,not
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True


# even odd ex
# 3%2 -> 1
# 4%2 -> 0
# 5%2 -> 1
# 6%2 -> 0
# 7%2 -> 1
# 8%2 -> 0

# multiple of 3 and 5
# 3%3 -> 0
# 5%5 -> 0
# 15%3 -> 0
# 15%5 -> 0


# strings
# string is a immutable ordered sequence of characters
s="hello world"
s2='python programming'
s3='''python programming'''
s4="""python programming"""
print(s)
print(s2)
print(s3)
print(s4)

a='this isn\'t a normal string'

# string operations
# concatenation(+)
# repetition(*)

# indexing
# slicing

first_name="john"
last_name="doe"
full_name=first_name+" "+last_name
print(full_name)

print(first_name*5) # johnjohnjohn
print("siddharth"*10)

'''
# Indexing
s="pramanicus"
# p r a m a n i c u s
# 0 1 2 3 4 5 6 7 8 9
#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# syntax
# variable_name[index]
print(s[3])
print(s[3])

print(s[-1])
print(s[-2])

# Slicing
# syntax
# variable_name[start_index:end_index]
# end_index is exclusive

s="pramanicus"
print(s[2:5]) # ama
print(s[2:]) # macus
print(s[:5]) # prama
print(s[:]) # pramanicus

# syntax
# variable_name[start_index:end_index:step]
print(s[2:8:2]) # amc
print(s[::2])
print(s[::3])
print(s[::-1])

# f-strings
name="john"
age=30
print("my name is " + name + " and my age is " + str(age))

print(f"my name is {name} and my age is {age}")

# string methods
# syntax
# variable_name.method()

# upper() - converts the string to uppercase
# lower() - converts the string to lowercase
# title() - converts the first character of each word to uppercase
# strip() - removes leading and trailing whitespace
# replace() - replaces a substring with another substring
# capitalize() - converts the first character of the string to uppercase and the rest to lowercase
# isalpha() - returns True if all characters in the string are alphabetic
# isdigit() - returns True if all characters in the string are digits
s="Hello World"
s2="welcome to python programming classes  "
print(s.upper()) # HELLO WORLD
print(s.lower()) # hello world
print(s2.title()) # Welcome To Python Programming Classes
print(s2.strip()) # welcome to python programming classes
print(s.replace("o","0")) # Hell0 W0rld
print(s.capitalize()) # Hello world
print(s.isalpha()) # False
print(s.isdigit()) # False

# Escape characters
# \n - new line
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote
# \r - carriage return
# \b - backspace

print("hello\nworld")
print('hello\tworld')
print("hello \"w\"orld")
print("hello\rwor")
print("hello\bworld")
print("hel\\")
# Membership operators
# in and not in
s="hello world"
print("hello" in s) # True
print("world" not in s) # False

# Basic data types
# int - integer
# float - decimal
# str - string
# bool - boolean

# Data structures types
# list, tuple, set, dictionary

'''