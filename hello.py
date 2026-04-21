print("welcome to python")
print(5+4)
print(5-4)
print(5*4)
print(5/2)
#print("5/2")

# print() is a in-built python function
# this is a comment
# there are two types of comments in python
# 1. single line comment (#)
# 2. multi line comment(''' or """)

"""
print("python students: charan, nitish,sai ram, ahmed and naveen")
print("python students: charan, nitish,sai ram, ahmed and naveen")
print("python students: charan, nitish,sai ram, ahmed and naveen")
"""
# this is a comment
# syntax = grammer

print(10%3)
print(10//3)
print(3**2)
print(3**3)


# population density
# d=p/a
print(16000000/650)


# f=1.8*c+32 , c=35
print(1.8*35+32)
print(1.8*40+32)

# sum of first n natural numbers
# n*(n+1)/2
# n=4, 1,2,3,4=10
# n=10, 1,2,3...8,9,10=55
# n=15
print(10*(10+1)/2)
print(4*(4+1)/2)
print(15*(15+1)/2)

# variables
# let x=10
# a name to a value
a=10
b=20
print(a)
print(b)

c=35
f=1.8*c+32
print(f)

c=40
f=1.8*c+32
print(f)

# arithmetic operators
# +, -, *, /, //(floor division), **(exponentiation), %(modulus)

# Assignment operator
# =, +=, -=, *=, /=, //=, **=, %=

x=5
x+=3 # x=x+3
print(x)

x-=2 # x=x-2
print(x)

x*=4 # x=x*4
print(x)

x/=2 # x=x/2
print(x) # 12.0

x//=3 # x=x//3
print(x) # 4.0

x**=2 # x=x**2
print(x) # 16.0

x%=5 # x=x%5
print(x)

x+=3
print(x)

temp=35
age=20
age2=21
salary=20000
hyd_temp=40
mumbai_temp=35


# Data types
# 1. int - integer
# 2. float - decimal numbers
# 3. str - string
# 4. bool - boolean (True or False)

a=10
b=3.14

print(type(a))
print(type(b))
print(type(10))
print(type(10.5))

# literals
# 1. int literal - 10, 20, -5
# 2. float literal - 3.14, -0.5

c="hello"
print(type(c))
d=True
e=False
print(type(d))
print(type(e))

# Type conversion
# implicit type conversion - python automatically converts one data type to another
# explicit type conversion - we manually convert one data type to another using built-in functions like int(), float(), str(), bool()
a=10
b=float(a)
print(b)

a=10.5
b=int(a)
print(b)

# int() is mainly used when you want to convert a string to an integer
a="10"
b=int(a) # "10" -> 10
print(b)
print(b+5) 

a="10.5"
# b=int(a) # "10.5" -> error
b=float(a) # "10.5" -> 10.5
print(b+1)

print(int(10.5))
print(int(10))
print(int("10"))
# print(int("10.5")) # error

print(float(10))
print(float(10.5))
print(float("10"))
print(float("10.5"))

# str()
print(str(10)) # "10"
print(str(10.5)) # "10.5"
print(str(True)) # "True"
print(str(False)) # "False"
print(str(b)) # "10.5"
print(str("z")) # "z"
# print(str(z))

# bool()
print(bool(0)) # False
print(bool(0.0)) # False
print(bool("")) # False
print(bool(1)) # True
print(bool(-1)) # True
print(bool("hello")) # True

print()

# Comparison operators
# ==, !=, >, <, >=, <=
print(10==11) # False 
print(10!=10) # False
print(10>5) # True
print(10<5.5) # False
print(10>=10) # True
print(10<=10) # True

a=(10==1)
print(type(a))



# Logical operators
# and, or, not

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # zFalse

print(not True) # False
print(not False) # True 

# Strings
# String is a immutable ordered sequence of characters
# They are used to represent text

s="hello"
s2='world'
s3="""python 
is a 
programming language"""
s4='''python 
is a programming 
language'''
print(s)
print(s2)
print(s3)
print(s4)

quotation = '"Knowledge is power"'
print(quotation) # "Knowledge is power"

quotation = "\"Knowledge is power\""
print(quotation) # "Knowledge is power"
# Escape characters
# \n - new line
# \t - tab
# \\ - backslash
# \" - double quote
# \' - single quote
# \r - carriage return
# \b - backspace
s5="hello\\new world"
print(s5) # hello\world
print("hello\nworld") # hello
print("hello\n\nwor\nld") # hello
print("hello\tworld") # hello   world
print("hello\t\tworld") # hello    world
print("hello world\rworld") # hello    world

# len()
# returns the length of the string
s="hello"
print(len(s)) # 5
s3="python language"
print(len(s3)) # 15

# String indexing and slicing
s="pramanicus"
# p r a m a n i c u s
# 0 1 2 3 4 5 6 7 8 9
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# syntax to access a character in a string
# str_var[index]
print(s[0]) # p
print(s[5]) # n
print(s[6]) # i
print(s[-10]) # p

s2="python language"
print(s2[1]) # y
print(s2[6])
print(s2[-1])
l=len(s2)
print(s2[l-14])
# print(s2[100])


# slicing
# syntax to slice a string
# str_var[start:end:step]
# end is exclusive 
s2="python language"
print(s2[0:6])
print(s2[7:15])

print(s2[-15:-8])
print(s2[4:6])

print(s2[0:6:2]) # pto
print(s2[7:15:3]) # lgg
print(s2[7:15:4]) # lu

print(s2[:6])
print(s2[7:])
print(s2[:])

print(s2[::2]) 
print(s2[::-1])
print(s2[::-2])

# String operations
# concatenation(+)
# repetition(*)
s1="hello"
s2="world"
print(s1+s2) # helloworld
s3=s1+s2+s1
print(s3) # helloworldhello
s4=s1+" "+s2
print(s4) # hello world

print(s1*3) # hellohellohello
print(s2*2) # worldworld

# string methods