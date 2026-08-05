# import functools

# # Step 1: basic decorator structure
# def my_decorator(func):
#     # @functools.wraps(func)     # preserves func's name and docstring
#     def wrapper(*args, **kwargs): #("alice") {}
#         print("Before the function")
#         result = func(*args, **kwargs)   # call the original function
#         print("After the function")
#         return result
#     return wrapper

# # Apply with @
# @my_decorator
# def greet(name):
#     print(f"Hello, {name}!")

# # greet=my_decorator(greet)

# greet("Alice")
# print(greet.__name__)  # greet


import functools, time

def timer(func):
    """Print the execution time of the decorated function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"[timer] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

# @timer
# def slow_sum(n):
#     return sum(range(n))

# slow_sum(10_000_000_000)
# 0.2*1000=200.0s



# Logger — log function calls
import functools
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        print(f"Calling {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"→ returned {result!r}")
        # !r - repr
        return result
    return wrapper

# @logger
# def add(a, b):
#     return a + b

# add(3, 5)
# add(1, 4)


@timer
@logger
def multiply(a, b):
    return a * b

multiply(3, 5)


# multiply=repeat(2)(multiply)
# multiply=decorator(multiply)

import functools

def repeat(n):
    """Decorator factory: repeat the function n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(10)
def say_hello():
    print("Hello!")


say_hello()


# Retry decorator — retry on failure
def retry(max_attempts=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise 
        return wrapper
    return decorator

@retry(max_attempts=3)
def flaky_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network timeout")
    return "Success!"

flaky_api_call()