tup = (1,)
print(type(tup), tup)

# to find length of tuple
print(len(tup))

tup_1 = (1, 2, 3, 4, True, False, "Akshat", "Dwivedi")
print(tup_1)


# to find something in tuple or give any condition
if "Akshat" in tup_1:
    print("Name exists")


# slicing is same as string or sets

print(tup_1[0:])
print(tup_1[0:-1])
print(tup_1[:])
