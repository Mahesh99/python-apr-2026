import random
# functions
# a function is a block of code that performs a specific task

# syntax
# function definition
# def function_name(parameters):
#     statement1
#     statement2
#     ...
#     statement N

# function call
# function_name(arguments)

# Example 1
def greet():
    print("Hello World!")
    print("Hello World 2!")

greet()
greet()
# greet()

# Example 2
def add(a, b):
    c = a + b
    return c

result = add(5, 3)
print("The sum is:", result)

result = add(10, 20)
print("The sum is:", result)


# Example 3
def print_hello():
    print("Hello, World!")

print_hello()
print_hello()
print_hello()


def loan_eligibility(age, income):
    if age >= 18 and income >= 30000:
        return "Eligible for loan"
    else:
        return "Not eligible for loan"

# age = int(input("Enter your age: "))
# income = int(input("Enter your income: "))
# loan_status = loan_eligibility(age, income)  
# print("Loan status:", loan_status)


"""
Based on the arguments, a function can be classified into the following categories:
1. Positional arguments
2. Default arguments
3. Variable-length arguments
4. variable-length keyword arguments
"""
# Default arguments
def greet(name="Guest"):
    print("Hello, " + name + "!")

greet()
greet("Alice")
greet("Bob")


def calculate_area(radius, pi=3.14):
    area = pi * radius ** 2
    return area

# Pi value upto 10 decimal places is 3.1415926535
area = calculate_area(5)
print("The area is:", area)

area = calculate_area(5, 3.1415926535)
print("The area is:", area)

area = calculate_area(radius=5, pi=3.1415926535)
print("The area is:", area)


# there can be more than one default argument in a function
def greet(name="Guest", greeting="Hello"):
    print(greeting + ", " + name + "!")

greet()
greet("Alice")
greet("Bob", "Hi")
greet(greeting="Hey")

# you can call function with keyword arguments
greet(greeting="Welcome", name="Charlie")


# Variable-length arguments
def sum_numbers(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print("The sum is:", result)

result = sum_numbers(10, 20, 30)
print("The sum is:", result)


# variable-length keyword arguments
def print_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print_info(name="Bob", profession="Engineer", country="USA")


def mix_of_arguments(a,b,c=10,d=20, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("args:", args)
    print("kwargs:", kwargs)


mix_of_arguments(1, 2)
mix_of_arguments(1, 2, 3)
mix_of_arguments(1, 2, 3, 4)
mix_of_arguments(1, 2, 3, 4, 5, 6, 7)
mix_of_arguments(1, 2, 3, 4, 5, 6, 7, name="Alice", age=30)
mix_of_arguments(1, 2, d=40, c=20,name="Alice", age=30)
mix_of_arguments(d=40, c=20,name="Alice", age=30,a=1,b=2)
mix_of_arguments(1, 2, 5, 6, 7,name="Alice", age=30)

#unpacking
j=[1,2,3,4,5]
mix_of_arguments(*j)


def mind_reader():
    r=random.randint(1,10)
    v=random.randint(2,4)
    print("Choose a number between 1 and 10")
    input()
    print("Multiply the result by ",v)
    input()
    print("Add ",r)
    input()
    print("Divide the result by ",v)
    input() 
    print("Subract your number from the result")
    input()
    print("Are you left with ",r/v)

# mind_reader()
# mind_reader()
# mind_reader()


# Recursion
# A function that calls itself is called a recursive function. Recursion is a programming technique where a function solves a problem by breaking it down into smaller subproblems of the same type. Each recursive call reduces the size of the problem until it reaches a base case, which is a simple case that can be solved directly without further recursion.


# n=int(input("Enter a number to find its factorial: "))
n=5
fact=1
for i in range(1, n+1):
    fact *= i

print("Factorial of", n, "is", fact)


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

# n=int(input("Enter a number to find its factorial: "))
# print("Factorial of", n, "is", fact(n))

"""
fact(5)
return 5*fact(4)

fact(4)
return 4*fact(3)


fact(3)
return 3*fact(2)

fact(2)
return 2*fact(1)

fact(1)
return 1
"""


# Lambda functions
cube = lambda x: x**3

print(cube(3))
print(cube(5))
c2f = lambda c: (c * 9/5) + 32
print(c2f(0))
print(c2f(37.4))

add = lambda a, b: a + b
print(add(5, 3))

ab3=lambda a, b: f'(a+b)^3={a**3+3*a*b**2+3*a**2*b+b**3}'
print(ab3(1,2))

l=["a11","z2","k7","14","b4","1","4"]
s='a11'
k=int(s[1:])
print(type(k),k)


def test(x):
    if x.isdigit():
        return int(x)
    else:
        return int(x[1:])

# l.sort(key=lambda x:int(x[1:]))
# l.sort(key=test)
# print(l)

k=filter(lambda x: True if x.isdigit() else False, l)
print(list(k))

k=map(lambda x: "Num" if x.isdigit() else "Not Num", l)
print(list(k))


employees = [{
                "name":"Sravan",
                "age":25,
                "salary":30000
             },
             {
                "name":"Rahul",
                "age":27,
                "salary":32000
             },
             {
                "name":"Keerthana",
                "age":23,
                "salary":35000
             }
            ]

sals=map(lambda x:x['salary'],employees)
sals=list(sals)
print(sals)
print(sum(sals)/len(sals))