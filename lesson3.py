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

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
loan_status = loan_eligibility(age, income)  
print("Loan status:", loan_status)
