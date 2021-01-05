from random import randint

gn=int(input("Enter number between 1 to 5 ="))
rn= randint(1,5)

if gn==rn:
    print("You have won")
else :
    print("You have loss")
