# this is used to make list on the go


list_1 = [i for i in range(1, 11)]
print(list_1)


# we can also add expression in this
list_2 = [i*i for i in range(1, 11)]
print(list_2)


# we can also add condition in list
list_2 = [i for i in range(1, 11) if (i % 2 == 0)]
print(list_2)


list_2 = [i for i in range(1, 11)]
print(list_2)

# i is stored in the list for purpose
list_3 = [i*1 for i in range(1, 11)]

# using list comprension with condition

list_4 = [i for i in range(10, 101) if (i % 2 == 0)]
print(list_4)
