class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name is {self.name} and id is {self.id}")

# inheritance


class employee_extends(employee):
    def get_info(self):
        print(
            f"This is extended class and employee name is {self.name} and his id is {self.id}")


e1 = employee("Akshat", 2255)
e1.showDetails()

e2 = employee_extends("Dwivedi", 255)
e2.get_info()
