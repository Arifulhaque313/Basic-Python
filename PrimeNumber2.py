num=int(input("Enter the value of a number : "))


if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("Not a prime no ")
            break
    else:
        print("its a prime number")
else:
    print("not a prime ")
