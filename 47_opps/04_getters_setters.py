class myClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"The value is {self.value}")

    # getter
    @property
    def myClass_setter(self):
        return self.value

    # @propert
    # def property_setter_1(self, value_2):
    #     self.value = value_2
    @myClass_setter.setter
    def myClass_setter(self, new_value):
        self.value = new_value


obj = myClass(10)
obj.myClass_setter = 20
print(obj.myClass_setter)
obj.show()
