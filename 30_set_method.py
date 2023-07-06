set_1 = {1, 2, 3, 4, 5}
set_2 = {5, 6, 7, 8}
# set_1 and set_2 are unchanged
print(set_1.union(set_2))

# update function
# update set_1
set_1.update(set_2)
print(set_1)

# to print common element in set
set_1 = {1, 2, 3, 4, 5, "Akshat"}
set_2 = {5, 1, 6, 7, 8, "Akshat"}
set_1.intersection_update(set_2)
print(set_1)

# to mutuate the set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)


# difference
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities)


# to check if disjoint
cities = {"Tokyo1", "Madrid2", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


# to check if element are common in suoerset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi", "Seoul", "Kabul"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))


# to add something in the set
cities2 = {"Seoul", "Kabul"}
cities2.add("Dewas")
print(cities2)


# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

cities2.remove("Dewas")
print(cities2)

cities2.discard("Dewas")
print(cities2)


# to pop something from last
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


# to delete an entire set
del cities

# to clear a set we use clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
