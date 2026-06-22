n=input("Enter a number:")

sum=0
for d in n: #153
    sum+=int(d)**len(n)

if int(n)==sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

"""
sum=0
d='1'
sum+=int(d)**len(n) = 1**3 = 1

d='5'
sum+=int(d)**len(n) = 5**3 = 125

d='3'
sum+=int(d)**len(n) = 3**3 = 27

sum=1+125+27 = 153
"""