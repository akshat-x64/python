class parent_class:
    def parent_method(self):
        print("This is a parent method")


class child_class(parent_class):
    def parent_method(self):
        print("Akshat")
        super().parent_method()

    def child_method(self):
        print("This is a child class")
        super().parent_method()


child_object = child_class()
child_object.child_method()
child_object.parent_method()


# super keyword in constructor method


class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class dev(employee):
    def __init__(self, name, id, pay):
        super().__init__(name, id)
        self.pay = pay


e2 = dev("akshat", 21, 33)
print(e2.__dict__)
