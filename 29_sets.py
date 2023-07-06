# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

# sets can have different type of datatypes
set_1 = {1, 2, 3, 4, 4, 4, 4}
print(set_1)
set_2 = {1, 2, 3, 4, 4, 4, 4, True, False}
print(set_2)

# how to create empty set
set_3 = set()
print(type(set_3))


for i in set_1:
    print(i)
