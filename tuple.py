
#Tuple_Practice
tuple_name=()
list=list(tuple_name)
list.append("ariful")
list.append("islam")
list.append("sajib")

tuple_name=tuple(list)
print(tuple_name)

print(tuple_name[1])

list=list(tuple_name)
list[1]="likhon"
tuple_name=tuple(list)
print(tuple_name)