list_1 = [1, 2, 4, 10]

# to add element from back in list we use append method

list_1.append(6)
print(list_1)


# to sort element in list we use sort method

list_1.sort()
print(list_1)

# to sort element in decreasing order

list_1.sort(reverse=True)
print(list_1)


# to reverse the list we use just reverse no sorting of any kind just plane reverse

list_1.reverse()
print(list_1)


# to find index in list of element

print(list_1.index(1))

# to count any element in list we use count method

print(list_1.count(1))


# to copy one list to another in the we use the copy function

list_2 = list_1.copy()
print(list_2)


# to insert element at given element we use insert method
print(list_2)
# (index,value)
list_2.insert(0, 212)


# to concat 2 list we can use extend method
list_1.extend(list_2)
print(list_1)

list_3 = list_1.copy() + list_2.copy()
print(list_3)
