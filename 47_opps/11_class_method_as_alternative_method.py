class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_str(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])


e = employee("harry", "12000")
print(e.name, e.salary)

String_1 = "Akshat-2000"
e1 = employee(String_1.split("-")[0], String_1.split("-")[1])
print(e1.name, e1.salary)
String_1 = "Dwivedi-2000"
e2 = employee.from_str(String_1)
print(e2.name, e2.salary)
