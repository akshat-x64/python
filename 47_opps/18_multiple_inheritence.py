class employee:
    def __init__(self, name):
        self.name = name


class dancer:
    def __init__(self, dance):
        self.dance = dance


class employee_dance(employee, dancer):

    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

    def __str__(self):
        return f"{self.name} will perform the {self.dance}"


e1 = employee_dance("Akshat", "Dance")
print(e1)

# to find out every thing about
# method resolution order
print(employee_dance.mro())
