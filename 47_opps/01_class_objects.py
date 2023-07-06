class person:
    first_name = "Akshat"
    last_name = "Dwivedi"
    age = 23
    occupation = "automation engineer"

    def info(self):
        print(
            f"My name is {self.first_name,self.last_name} and ,my age is {self.age}and my occupation is {self.occupation}")


a = person()
a.info()
print(a.first_name, a.last_name, a.age, a.occupation)
b = person()
b.first_name = "ram"
b.info()
print(b.first_name, b.last_name, b.age, b.occupation)


# Python Class and Objects

# Aclass is a blueprint or a template for creating objects, providing initial values
# for state (member variables or attributes), and implementations of behavior
# (member functions or methods). The user-defined objects are created using
# the class keyword.


# self parameter

# The self parameter is a reference to the current instance of the class, and is
# used to access variables that belongs to the class.


# It must be provided as the extra parameter inside the method definition.
