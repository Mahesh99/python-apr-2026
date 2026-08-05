f=open("data.txt","r")
print(f.readlines())
f.close()

# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Hello, World!\n")
#     f.write("Second line\n")
#     f.writelines(["line3\n", "line4\n"])

# with open("log.txt", "a") as f:
#     f.write("New log entry\n")

# with open("test.txt",'x') as f:
#     pass

#with open('Untitled.png','rb') as f:
#    print(f.read())

#import csv

# Read as a list of rows (each row is a list)
# with open("students.csv", newline="") as f:
#    reader = csv.reader(f)
#    header = next(reader)   # skip header row
#    for row in reader:
#        print(row)    


# with open("students.csv", newline="") as f:
#    reader = csv.DictReader(f)
#    students = list(reader) 

# import csv

# with open("students.csv", newline="") as f:
#     reader = csv.DictReader(f)
#     students = list(reader)   # list of OrderedDict
# print(students)
# for s in students:
#     print(s["Name"], s["Score"], s["Age"])