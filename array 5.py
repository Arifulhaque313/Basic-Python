from array import *
a=[]

n=int(input("Enter how many elements ="))

for i in range (n):
    data=int(input("enter the next elements ="))
    a.append(data)
print(a)
for i in range (n):
    x=a.sort()

print(a)
