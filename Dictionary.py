
new_dictionary={ "name":"sajib","age":24,"salary":6000}

print (new_dictionary)
print(new_dictionary.get("age"))

print("My name is " +new_dictionary["name"])

new_dictionary.pop("age")

print ("After remove age : "+str(new_dictionary))

#print all the keys
print(new_dictionary.keys())

#print all the values

print(new_dictionary.values())

new_variable=10
new1_dictionary={"name":new_variable}

print(new1_dictionary)



sajib={
    "name":"sajib",
    "age":30,
    "salary":6000
}

print("all the elements of the list is  : " +str(sajib))

updateAge={"age":22}
sajib.update(updateAge)

print("After update all the elements of the list is  : " +str(sajib))

print("Show me all the keys of the dictionary is = "+str(sajib.keys()))
print("Show me all the values of the dictionary is = "+str(sajib.values()))
