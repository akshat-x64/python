list_example = [1, 2, 3, 4, "Akshat", "Dwivedi"]
print(type(list_example))
print(list_example[0])
print(list_example[1])
print(list_example[2])
print(list_example[3])
print(list_example[4])
print(list_example[5])


print("----------------indexing in python list----------- ")


print(list_example[-3])


print("-----------------find something in python list--------")
if "Akshat" in list_example:
    print("yes")
else:
    print("no")


# slicing


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in list_1:
    print(i)


print(list_1)
print(list_1[1:7])


print(list_1[1:7:2])
# 2 is jump index it will skip 2 elements
