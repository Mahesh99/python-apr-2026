first_ten = [1,1,2,3,5,8,13,21,34,55]

def fib(n):
    if n==1:
        print("1")
    elif n==2:
        print("1 1")
    else:
        a, b = 1, 1
        print("1 1", end=" ")
        for _ in range(2, n):
            a, b = b, a + b
            print(b, end=" ")
        print()  # for newline after printing the sequence

def fib2(n):
    if n==1:
        return [1]
    elif n==2:
        return [1, 1]
    else:
        a, b = 1, 1
        result = [a, b]
        for _ in range(2, n):
            a, b = b, a + b
            result.append(b)
        return result
    
if __name__ == "__main__":
    fib(5)
    print(fib2(5))
    print(__name__)
