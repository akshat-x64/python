tup_sample = ("India", "Australia", "Japan", "South Korea", "Singapore")
print(tup_sample)
temp = list(tup_sample)
temp.append("Tiwan")
temp.pop(1)
temp[2] = "Finland"
tup_sample = tuple(temp)

print(tup_sample)

tup_con = tup_sample + ("AKshat", "Dwivedi", "AKshat")
print(tup_con)


# count an element in an tuple
print(tup_con.count("AKshat"))


# to find index of an elemet with silcing
print(tup_con.index("AKshat"))
print(tup_con.index("AKshat", 6, len(tup_con)))
