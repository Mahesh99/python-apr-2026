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