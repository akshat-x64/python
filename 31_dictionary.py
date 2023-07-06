# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dictionary = {
    "Name": "Akshat",
    "lastName": "Dwivedi"
}

print(dictionary["Name"])

employee_id = {
    # key #values
    1: "AKshat",
    2: "Ankit",
    3: "Ankit",

}
print(employee_id[1])

# to get value without error we can get
print(employee_id.get(12))


# how to get all keys in the dictionary
print(employee_id.keys())

# how to get all values in the dictionary
print(employee_id.values())

# to get all the data from the dictionary
print(employee_id.items())


# to print all the key from the dictionary
for i in employee_id.keys():
    print(f"This is {i} in i for {employee_id[i]}")

# to print all the key from the dictionary
for key, value in employee_id.items():
    print(f"This is key({key}) in i for {value}")
