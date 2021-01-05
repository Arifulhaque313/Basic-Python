arr=[]
sum=0
n=int(input("Enter the length of the value ="))
for i in range(n):
    d=int(input("Enter the next value = "))
    arr.append(d)
    sum=sum+d
print("The array is =",arr)
print("The sum of this array values is =",sum)
