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
def greet(name):
    print("Hello, " + name + "!")

greet("John")
greet("Alice")
greet("Bob")
print("End of program")
greet("Charlie")

# Example 2
def add(a, b):
    return a + b

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

