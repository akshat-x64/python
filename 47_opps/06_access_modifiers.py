# Access Specifiers/Modifiers
# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers
# Public access modifier
# Private access modifier
# Protected access modifier

# public access modifier

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # def get_info(self):
    #     print(f"This is {self.name} and id is {self.id}")


e1 = employee("Akshat", 23)
print(e1.name)

# private access modifier


class student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id


s1 = student("Akshat", 20)

# print(s1.name) cannot be accessed directly
# but can be accessed indirectly

print(s1._student__name)

# to find out which methods a object can have to find it out we have
print(s1.__dir__())


# protected access modifier

class student_1:
    def __init__(self):
        self._name = "Akshat"

    def _funNmae(self):
        return "code with akshat"


class subject(student_1):
    pass


obj_1 = student_1()
obj_2 = subject()

# calling
print(obj_1._name)
print(obj_1._funNmae())
# calling o2
print(obj_2._name)
print(obj_2._funNmae())
