friends = "mango"
# string splicing
# to print the length of the string
# we use
print(len(friends))
print(friends[0:3])

print(friends[1:3])

print(friends[0:-3])

print(friends[-3:-1])

nm = 'harry'
print(nm[-4:-2])

# this all methods dosen't mutute it returns a new string
# convert string to uppercase

print(friends.upper())

# convert string to lowercase

print(friends.lower())

# to remove something from right to the string
print("----------------------------------------------------------------")
sample = "--- Akshat ---"
print(sample.rstrip("-"))


# to replace a word or letter in the string

print(sample.replace("-", ""))

# to split someting in the string into list

print(sample.split(" "))


# to capitalise a letter int the string
num_1 = "greatest show ever"
print(num_1.capitalize())

# to convert string to center

str_1 = "This is a sample test"
print(str_1.center(80))


# to count something in the string

str_2 = "akshat akshat akshat"
print(str_2.count("akshat"))

# to check if string ends with something
str3 = "AKshatD"
print(str3.endswith('D'))

# to check if something ends with

str3 = "Akshat is a software engineer"
print(str3.find("is a", 0, len(str3)))


# to check if a string is in lowercase or not
print(str3.lower().islower())


# to check if all characters are printable or not
str3 = "Akshat is a software engineer\n"
print(str3.isprintable())


# to check if white soaces exist or not
print("   ".isspace())


# to check is all lettes are capital in string or not
print("This Is A Sampple Test".istitle())


# to swap case converts upper to lower or lower to upper case

print("Akshat".swapcase())


# to convert string to title case

print("Akshat is a software engineer".title())


print("--------- to find something in string---------")

str__1 = "Akshat"
if "Ak" in str__1:
    print("yes")
else:
    print("no")


aa = "Akshat"
print(aa.swapcase())