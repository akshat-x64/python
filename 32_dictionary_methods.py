ep_1 = {
    1: 23,
    2: 22,
    3: 99,
    4: 100
}
ep_2 = {
    4: 23,
    5: 22,
    6: 99,
    7: 100
}
# to merge 2 dictionary
ep_1.update(ep_2)
print(ep_1)

# to empty a dictionary
ep_1.clear()
print(ep_1)

# to make empty dictionary
ep_test = {}
print(type(ep_test))

# to delete anything from the dictionary

ep_1 = {
    1: 23,
    2: 22,
    3: 99,
    4: 100
}
ep_1.pop(1)
print(ep_1)

# to remove the lastelement from the dictionary
ep_1.popitem()
print(ep_1)


ep_1 = {
    1: 23,
    2: 22,
    3: 99,
    4: 100
}

# to delete entire key
del ep_1[1]
print(ep_1)


# to delete entire dictionary items
# del ep_1
print(ep_1)
