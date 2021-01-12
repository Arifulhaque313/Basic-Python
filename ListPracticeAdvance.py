
#List _____________

listname=[]

listname.extend([1,2,3,4,5,"hellow"])

print (listname)

listname.append(4)
print(listname)

listname.remove("hellow")
print (listname)


if 7 in listname :
        print ("yes ")
else:
       print ("no")



ch=(input("Enter a charecter : "))

if ch=="a" or ch=="e"or ch=="i" or ch=="o" or ch=="u" :
    print ("vowel")
else:
    print("consonant")


list2=list(("arif","murad","liton","Aklima"))
print(list2)