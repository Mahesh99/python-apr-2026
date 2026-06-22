# 1 1 2 3 5 8 13 21 34 55 ...
#       a b c
n=int(input("Enter a number:"))

if n==1:
    print("1")
elif n==2:
    print("1 1")
else:
    print("1 1",end=" ")
    a = 1
    b = 1
    for i in range(3,n+1):
        c = a + b
        print(c, end=" ")
        a=b
        b=c