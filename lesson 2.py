battery=7
if battery<=20:
    print("Battery is low")
    print("Please connect the charger")


marks=2
if marks==25:
    print("Good")
else:
    print("Bad")
    print("Can do better")

# what all are considered false?
# False, None, 0, 0.0, "", [], (), {}, set(), range(0), range(1, 0)


if 1:
    print("hi")

# if, elif,.. else

marks_scored=80

if marks_scored>=90:
    print("Grade A")
elif marks_scored>=80:
    print("Grade B")
elif marks_scored>=70:
    print("Grade C")
elif marks_scored>=35:
    print("No grade")
else:
    print("Fail")


a = 10
if a%3 == 0:
    if a%5 == 0:
        print(str(a),"is a multiple of 3 and 5")
    else:
        print(str(a),"is not a multiple of 3 and 5")
else:
    print("Not a multiple of 3 and 5")



# Loops
# when you want to execute a block of code multiple times
# for loop
# while loop

# for loop
# syntax
# for variable in sequence:
#     statement1
#     statement2
#     ...
#     statement N

l =[1,2,3,4,5]
for i in l:
    print(i)
    print("--")

d={"name":"John","age":30,"city":"New York"}
for key in d:
    print(key)
    print(d[key])   

s="pramanicus,python"
for i in s:
    print(i)

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

# range() function
# range(start, stop, step)
# start - optional, default is 0
# stop - required
# step - optional, default is 1
# range(10) - range(stop)
# range(1,11) - range(start, stop)
# range(1,11,2) - range(start, stop, step)

for i in range(10):
    print(i)

for i in range(100):
    print(i, end=" ")

print()
for i in range(1,11):
    print(i)
print()

for i in range(1,11,2):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(10,1,-1):
    print(i)

# when we don't know how many times we want to execute a block of code, we use a while loop
# while loop
# syntax
# while condition:
#     statement1
#     statement2
#     ...
#     statement N

print()
i=0
while i<10:
    print(i)
    i+=1

nums = {2,6,8,1,4,9,11,10,5}

my_nums = []

while sum(my_nums) <= 21:
    my_nums.append(nums.pop())

print(sum(my_nums))
print(my_nums)

# break and continue


# break
# terminates current and all further iterations of the loop


# Prime number
# 17
# 2 to 16
# 2 to 8
# n=int(input("Enter a number: "))
# flag=False

# for i in range(2,int(n/2+1)):
#     if n%i==0:
#         flag=True
#         break
        
# if flag:
#     print("Not prime")
# else:
#     print("Prime")


# continue
# skips the current iteration of the loop and moves to the next iteration

# Example 1
for i in range(10):
    if i == 5 or i == 7:
        continue
    print(i,end=" ")

print()
for i in range(1, 11):
    continue
    print(i)


# list comprehension
# syntax
# var = [expression for item in list]
# var = [expression for item in list if condition]

l = [i for i in range(10)]
print(l)

l = [i*2 for i in range(1,11)]
print(l)

l = [i for i in range(10) if i%2==0]
print(l)

l = [i for i in range(10) if i%2!=0]
print(l)

l =["even" if i%2==0 else "odd" for i in range(10)]
print(l)

l = [j for i in range(1,11) for j in range(1,i+1)]
print(l)

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# even odd

n=int(input("Enter a number: "))
if i%2==0:
    print("even")
else:
    print("odd")