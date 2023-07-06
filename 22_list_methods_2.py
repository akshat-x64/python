list_sample = [54, 23, 1235, 54, 23, 23, 4, 523, 32]
print(list_sample)

# to add element at back of the list
list_sample.append(23)
print(list_sample)

# to sort the list
list_sample.sort()
print(list_sample)

# to sort list in reverse order
list_sample.sort(reverse=True)
print(list_sample)

list_sample = [54, 23, 1235, 54, 23, 23, 4, 523, 32]

# to reverse the list without sorting the list
list_sample.reverse()
print(list_sample)

list_sample = [54, 23, 1235, 54, 23, 23, 4, 523, 32]

# to find index of given value
print(list_sample.index(23))


# to count the value of the element in list
print(list_sample.count(23))


# to copy one list to another list
list_sample2 = list_sample.copy()
print(list_sample2)


# how to insert elent at given list
list_sample.insert(0, 000)
print(list_sample)


# how to concat list
list_1 = [2, 34, 5, 6]
list_2 = [76, 43, 5, 32]

list_1.extend(list_2)
print(list_1)
print(list_1+list_2)
