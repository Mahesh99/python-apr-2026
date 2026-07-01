import random

r=random.randint(1,100)

turns=0
while True:
    n=int(input("Enter value:"))
    turns+=1
    if n==r:
        print(f"Congratulation! You guessed it right in {turns} turns!")
        break
    elif r<n:
        print("The number is smaller")
    else:
        print("The number is larger")
