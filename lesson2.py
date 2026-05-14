# conditional statements
# if statement
# if else statement
# if elif else statement

# nested if statement

# if statement
# syntax

# if condition:
#     statement1
#     statement2
#     ...
#     statement N

# statements inside the if block will only execute if the condition is true
# statements should be indented to indicate that they belong to the if block
# usualy we use 4 spaces(tab) for indentation in python(sometimes 2 spaces)

# Example 1
battery = 15
if battery <= 20:
    print("Battery is low")
    print("Please charge the battery")

# Example 2
age = 18
if age >= 18:
    print("You are eligible to vote")



# if else statement
# syntax
# if condition:
#     statement1
#     statement2
#     ...
#     statement N
# else:
#     statement1
#     statement2
#     ...
#    statement N

# Example 1
# even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Example 2
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")



# if elif else statement
# syntax
# if condition1:
#     ...
# elif condition2:
#     ...
# elif condition3:
#     ...
# else:
#     ...

# else block is optional in if elif else statement


# Example 1
# grade calculation
# marks = int(input("Enter your marks: "))
# if marks > 90:
#     print("Grade A")
# elif marks > 80:
#     print("Grade B")
# elif marks > 70:
#     print("Grade C")
# elif marks > 60:
#     print("Grade D")
# elif marks >= 35 and marks <= 60:
#     print("No grade")
# else:
#     print("Fail")



# nested if statement
# syntax
# if condition1:
#     if condition2:
#         statement1
#         statement2
#         ...
#         statement N


# Example 1
# age = int(input("Enter your age: "))
# if age >= 18:
#     if age <= 60:
#         print("You are eligible to vote")
#     else:
#         print("You are not eligible to vote")
# else:
#     print("You are not eligible to vote")



# mistakes in conditional statements
# applying proper indentation 

# what all are considered as true and false in python
# false - False, None, 0, 0.0, 0j, "", [], (), {}, set(), range(0), Decimal(0), Fraction(0, 1)
# true - all other values

a=""
if a:
    print("a is true")


# Loops
# for, while, nested loops
# loops are used to execute a block of code repeatedly until a certain condition is met

# for loop
# syntax
# for variable in sequence:
#     statement1
#     statement2
#     ...
#     statement N

# sequence can be a list, tuple, string, range, etc.

# Example 1
for i in range(5):
    print("hello")

# Example 2
for i in range(10): # 0 to 9
    print(i)

# range(start, stop, step)
# start - starting value of the sequence (default is 0)
# stop - ending value of the sequence (default is 1)
# step - difference between each number in the sequence (default is 1)

# range(stop)
# range(start, stop)
# range(start=0, stop, step=1)

print()
# Example 3
for i in range(1, 11): # 1 to 10
    print(i)

# Example 4
for i in range(1, 11, 2): # 1 to 10 with step 2
    print(i)

for i in range(1,11,3):
    print(i)

for i in range(2,11,2):
    print(i)

l = [11, 22, 33, 44, 55]
for i in l:
    print(i)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit, len(fruit))

p="python"
for char in p:
    print(char)


# program 
# Print percentage of marks obtained by a student in 5 subjects 
# marks = []
# for i in range(5):
#     mark = int(input(f"Enter marks for subject {i+1}: "))
#     marks.append(mark)

# total_marks = sum(marks)
# percentage = (total_marks / 500) * 100
# print(f"Total marks: {total_marks}")
# print(f"Percentage: {percentage:.2f}%")



# while
# syntax
# while condition:
#     statement1
#     statement2
#     ...
#     statement N

# statements inside the while block will only execute if the condition is true
# we use while loop when we don't know the number of iterations in advance

# Example 1
i = 0
while i < 10:
    print("hello")
    i += 1 

i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>=1:
    print(i)
    i-=1

# program
# sum of digits of a number
# 251
# 2 + 5 + 1 = 8
# 1671
# 1 + 6 + 7 + 1 = 15

# num = int(input("Enter a number: ")) # 251
# sum_of_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num //= 10
# print(f"Sum of digits: {sum_of_digits}")




# break and continue statements in loops
# break - used to exit the loop when a certain condition is met 
# continue - used to skip the current iteration of the loop

# Example 1
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5 or i == 7:
        continue
    print(i)


# infinite loop - a loop that never ends
# i=0
# while i>=0:
#     print(i)
#     i+=1


# nested loops
# a loop inside another loop
# Example 1
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


# list comprehension
# syntax
# [expression for item in iterable if condition]
# Example 1
# used to create a new list by applying an expression to each item in an iterable 

# squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)