import random

# import fibonoccimodule

# fibonoccimodule.fib(10)
# l=fibonoccimodule.fib2(10)
# print(l)
# print(fibonoccimodule.first_ten)




# import fibonoccimodule as fm

# fm.fib(10)
# l=fm.fib2(10)
# print(l)
# print(fm.first_ten)




# from fibonoccimodule import fib,first_ten

# fib(10)
# print(first_ten)




# from fibonoccimodule import fib as f,first_ten as ft

# f(10)
# print(ft)



# from fibonoccimodule import *
# fib(10)
# print(fib2(10))
# print(first_ten)


import test
import fibonoccimodule

# __name__
# print(dir(__builtins__))
print(__name__)

import sys
print(sys.path)



import random


r=random.randint(1,10)
print(r)

r=random.randrange(1,21);
print(r)

cards=[i for i in range(1,53)]
random.shuffle(cards)    
print(cards)

r=random.choice(cards)
print(r)

random.seed(10)
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))


# __init__.py

import swiggy.test
swiggy.test.dummy()

import test2
