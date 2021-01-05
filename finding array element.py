arr=[]

n=int(input("Enter the length of the value ="))
for i in range(n):
    d=int(input("Enter the next value = "))
    arr.append(d)
print("The array is =",arr)

key=int(input("Enter the key ="))
for i in range(n):
    if arr[i]==key:
        print(key,"Element is found and its positon is ",i+1)
        break;
else :
    print("Is not found ")



