class person:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"The name is {self.name} and occupation is {self.occupation}")


p1 = person("Akshat","Software engineer")
# p1.info()

# decerators
def greet(fx):
    def mfx():
        print("hello everyone")
        fx()
        print("Good bye everyone")
    return mfx


@greet
def hellop():
    print("hello world")

# hellop()

#getters setters
class person:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"This is the value of self{self.value}")

    @property
    def ten_value(self):
        return 10*self.value

    @ten_value.setter
    def ten_setter(self,new_value):
        self.value = new_value/10

p1 = person(10)
p1.ten_setter = 10
# print(p1.ten_value)

#static method

class maths:
    def __init__(self,n):
        self.n = n
    
    def add_num(self,aa):
        self.n  = n + aa
    
    @staticmethod
    def add_meth(a,b):
        return a+b

# print(maths.add_meth(10, 20))


#Class Methods as Alternative Constructors 

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.name = salary

e = employee("Akshat", 2000)
    

class employee_1:
    company = "Google"
    def __init__(self,name):
        self.name = name
    
    def info(self):
        print(f"this name of employee is {self.name} and {self.company}")

    @classmethod
    def change_company(aa,new_company):
        aa.company = new_company


e2 = employee_1("Akshat")
e2.info()
e2.change_company("Apple")
e2.info()


#Class Methods as Alternative Constructors in Python
class employee_2:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"the name of employee {self.name} and salary is {self.salary}")

    @classmethod
    def inputStr(aa,bb):
        return employee_2(bb.split("-")[0],bb.split("-")[1])


e = employee_2("AKshat", 28000)
string_1  = "harry-2000"

e1 = employee_2.inputStr(string_1)
e1.info()



#method overriding

class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14*super().area()



c1 = circle(24)
print(c1.area())