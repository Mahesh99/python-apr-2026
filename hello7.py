# print("Hello world")
# print("Welcome to python classes")
# print(3+4)
# print(3-4)
# print(3*4)
# print(5/2)
# print(5//2)
# print(5%2)
# print(5**2)



# s=input("Enter a word:")
# if s==s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

"""
def fib_slow(n):
    if n < 2: return n
    return fib_slow(n-1) + fib_slow(n-2)
# fib_slow(40) takes ~30 seconds
fib_slow(4)
return fib_slow(3) + fib_slow(2) = 2 + 1 = 3

fib_slow(3) = fib_slow(2) + fib_slow(1) = 1 + 1 = 2

fib_slow(2) = fib_slow(1) + fib_slow(0) = 1 + 0 = 1 

fib_slow(2) = fib_slow(1) + fib_slow(0) = 1 + 0 = 1

 o  |  x |   
____|____|____
 x  |  o |
____|____|____
    |  x |  o
    |    |  

states=["o","x"," ","x","o"," "," ","x","o"]
player 1 turn(x): 2
"""
print("Hello world",'hi','bye')
print("Hello world",'hi','bye')

from functools import partial

data   = [("Alice", 88), ("Bob", 72), ("Carol", 95)]
getkey = partial(lambda i, x: x[i],1)
print(sorted(data, key=getkey))

# print(getkey(("Alice", 88)))
# Write a generator primes() that yields prime numbers infinitely. Print the first 20 primes.

def primes():
    n=2
    while True:
        prime=True
        for i in range(2,(n//2)+1):
            if n%i==0:
                prime=False
                break
        if prime:
            yield n
        n+=1

g=primes()
for i in range(20):
    print(next(g))


