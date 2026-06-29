# Data Structures in Python
# List - ordered, mutable,sequence of elements
# Tuple - ordered, immutable, sequence of elements
# Set - unordered, mutable, no duplicate elements
# Dictionary - unordered, mutable, key-value pairs, no duplicate keys

# List
l = [1, 2, 3, 4, 5]
print(l)
print(type(l))

l2=["hello", 1, 2.5, True]
print(l2)

fruits = ["apple", "banana", "cherry", "date", "blueberry"]
print(fruits)

marks = [85, 90, 78, 92, 88]
print(marks)

# Indexing

# accessing elements using index
print(marks[0]) # 85
print(marks[1]) # 90

print(fruits[-1]) # blueberry
print(fruits[-2]) # date

# modifying elements
fruits[4]="grapes"
print(fruits)


# Slicing
marks=[85, 90, 78, 92, 88]
print(marks[1:4]) # [90, 78, 92]
print(marks[:3]) # [85, 90, 78]
print(marks[2:]) # [78, 92, 88]
print(marks[::2]) # [85, 78, 88]


# List functions
# len(), min(), max(), sum()
print(len(marks)) # 5
print(min(marks)) # 78
print(max(marks)) # 92
print(sum(marks)) # 433


# for strings min() and max() will return the lexicographically smallest and largest character respectively
print(len(fruits)) # 5
print(min(fruits)) # apple
print(max(fruits)) # grapes

# string method
s="welcome to python programming"
k=s.split() # splits the string into a list of words
print(k)

s2="apple,banana,cherry,date,grapes"
k2=s2.split(",") # splits the string into a list of fruits using comma as a separator
print(k2)

# print(dir(str))
# print(dir(list))

s3="--".join(k) # joins the list of words into a string using space as a separator
print(s3)

# list methods
# append(), insert(), remove(), pop(), sort(), reverse(), count(), index()

# append() - adds an element to the end of the list
# insert() - inserts an element at a specific index
# remove() - removes an element from the list
# pop() - removes an element from the end of the list
# sort() - sorts the list
# reverse() - reverses the order of the list
# count() - returns the number of occurrences of an element in the list
# index() - returns the index of the first occurrence of an element

marks=[85, 90, 78, 92, 88, 90,78]
marks.append(95)
print(marks)

marks.append(85)
print(marks)

marks.insert(2, 80)
print(marks)

marks.remove(80)
print(marks)

res=marks.pop()
print(marks,res)

marks.sort()
print(marks)

marks.reverse()
print(marks)

print(marks.count(78))

print(marks.index(78))

marks.extend([99,100, 100])
print(marks)

# Tuple
# They are similar to lists in the way they are created and accessed.
# Tuples are created using parenthesis - ()
# Tuples are mainly used when you have values which are closely related and their position matters
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))

t2=("hello", 1, 2.5, True)
print(t2)

# print(dir(tuple))
point = (4,3,11) # (x,y,z) coordinates in a 3d space
location = (17.393549, 78.533836) #(latitude, longitude)
dimens = 10,20,15 # (l,b,h) dimensions of a cuboid. Tuple can also be intialized this way

l,b,h = dimens # Tuple unpacking

# Set
# They are unordered, mutable, no duplicates
# set is an unordered mutable collection of unique elements

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

s1={1, 2, 3, 4, 5, 5, 5}
print(s1)

s2={3, 4, 5, 6, 7}
print(s2)

# union, intersection, difference
s4=s1.union(s2) # {1, 2, 3, 4, 5, 6, 7}
print(s4)

# intersection
s5=s1.intersection(s2) # {3, 4, 5}
print(s5)

# difference
s6=s1.difference(s2) # {1, 2}
print(s6)
print(s6.issubset(s1)) # True
print(s2.issuperset(s5)) # True
# print(dir(set))
# print(help(set.pop))


# Dictionary
# key-value pairs
# Dictionary is a mutable object which stores mappings of unique keys to values
# Keys can be of any type

d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(d)
print(type(d))

d2={'name': 'John', 'age': 30, 'city': 'New York', 'name': 'Jane'}
print(d2) # {'name': 'Jane', 'age': 30, 'city': 'New York'} - duplicate keys are not allowed. The last value will be considered

# accessing values using keys
student = {'name': 'Alice', 'age': 25, 'grade': 'A'}
print(student)
print(student['name']) # Alice
print(student['age']) # 25
print(student['grade']) # A

# modifying values
student['grade'] = 'A+'
print(student)

# adding a new key-value pair
student['major'] = 'Computer Science'
print(student)

# removing a key-value pair
del student['major']
print(student)

# del student
# print(student) # NameError: name 'student' is not defined


# dictionary methods
# keys(), values(), items(), get(), pop(), popitem(), clear()

d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(d.keys()) # dict_keys(['name', 'age', 'city'])
print(d.values()) # dict_values(['John', 30, 'New York'])
print(d.items()) # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

print(d.get('name')) # John
print(d.get('country')) # None
print(d.get('country',"Not Found")) # Not Found

print(d.pop('name')) # John
print(d) # {'age': 30, 'city': 'New York'}

print(d.popitem()) # ('city', 'New York')
print(d) # {'age': 30}

d.clear()
print(d) # {}

print(help(dict.popitem))


# Type conversion
v=list(student.values())
print(v)

print(list(student.items()))

l=[1,2,2,3,3,3,4,4,4,4]
s=list(set(l))
print(s)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(list(student))