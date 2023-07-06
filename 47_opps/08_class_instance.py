# class variable vs instance variable

class employee:
    companyName = "Google"
    employee_number = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        self.employee_number = self.employee_number+1

    def showDetails(self):
        print(
            f"The name of employee is {self.name} and company name is {self.companyName} and emplyees are {self.employee_number}")


emp1 = employee("Akshat")
emp1.raise_amount = 3.3
emp1.companyName = "Google India"
emp1.showDetails()
employee.companyName = "Apple"
# employee.showDetails(emp1)
emp2 = employee("Dwivedi")
emp2.companyName = "Google"
emp2.showDetails()
# print(dir(emp2))
print(employee.employee_number)
