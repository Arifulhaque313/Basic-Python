from array import *
arr=[]

n=int(input("Enter the length of the value ="))
for i in range(n):
    d=int(input("Enter the next value = "))
    arr.append(d)

print("The array is =",arr)

for i in range(n):
    arr.reverse()
print(arr)