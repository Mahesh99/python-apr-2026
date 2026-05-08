# Basic python data structures
# 1. List - ordered, mutable, allows duplicates
# 2. Tuple - ordered, immutable, allows duplicates
# 3. Set - unordered, mutable, no duplicates
# 4. Dictionary - unordered, mutable, key-value pairs, no duplicate keys

# List
# List is a mutable ordered sequence of elements
l = [1, 2, 3, 4, 5]
print(l)

fruits = ["apple", "banana", "papaya", "cherry"]
print(fruits)

r_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(r_list)

empt_list = []
print(empt_list)

# Indexing and slicing
print(l[3]) # 4
print(fruits[2]) # papaya

print(l[2:5]) # [3, 4, 5]
l2=l[2:5]
print(l2) # [3, 4, 5]

# list functions
# len(), min(), max(), sum()
print(len(l)) # 5
print(min(l)) # 1
print(max(l)) # 5
print(sum(l)) # 15
# print(min(r_list)) # TypeError: '<' not supported between instances of 'str' and 'int'
print(min(fruits)) 
print(max(fruits)) 

# modifying a list
l[0] = 10
print(l) # [10, 2, 3, 4, 5]
l[3:5] = [40, 50]
print(l) # [10, 2, 3, 40, 50]

# unpacking
a,b,c=[1,2,3]
print(a) # 1
print(b) # 2    
print(c) # 3

# list methods
l=[1, 2, 3, 4, 5]
# append() - adds an element to the end of the list
# pop() - removes and returns the last element of the list
# insert() - inserts an element at a specific index
# remove() - removes the first occurrence of an element
# sort() - sorts the list in ascending order
# reverse() - reverses the order of the list
# count() - returns the number of times an element appears in the list
# index() - returns the index of the first occurrence of an element
# clear() - removes all elements from the list
l.append(6)
print(l) # [1, 2, 3, 4, 5, 6]

a=l.pop()
print(l) # [1, 2, 3, 4, 5]
print(a) # 6

l.insert(3, 10)
print(l) # [1, 2, 3, 10, 4, 5]

l.remove(10)
print(l) # [1, 2, 3, 4, 5]

print()
l.sort()
print(l) # [1, 2, 3, 4, 5]

l.sort(reverse=True)
print(l) # [5, 4, 3, 2, 1]

l.reverse()
print(l) # [1, 2, 3, 4, 5]

l.append(5) # [1, 2, 3, 4, 5, 5]

print(l.count(5)) # 2

print(l.index(5)) # 4

l.clear()
print(l) # []