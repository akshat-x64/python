# magic method also known as dunder method

from typing import Any


class employee:
    name = "akshat"

    def __len__(self):
        i = 0
        for a in self.name:
            i = i+1
        return i

    # def __str__(self):
    #     return f"The employee name is {self.name}"

    def __repr__(self):
        return f"The employee name is {self.name} repr"

    def __call__(self):
        print(self.__class__)


e1 = employee()
print(len(e1))
print(str(e1))
print(repr(e1))
e1()
