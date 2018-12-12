class Employee:
    raise_amount= 1.04

    def __init__(self, first,last,pay):
        self.first=first
        self.last= last
        self.email= first+"."+last+"@company.com"
        self.pay=pay

    def fullName(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang= prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.fullName())


dev1= Developer("Corey", "Schafer", 50000,"Python")
dev2= Developer("Test", "User", 50000, "Java")

# print(dev1.email)
# print(dev1.prog_lang)

mngr1= Manager("Sue", "Smith", 90000, [dev1])
print(mngr1.email)
print(mngr1.print_emps())

mngr1.add_emp(dev2)
print(mngr1.print_emps())

mngr1.remove_emp(dev1)
print(mngr1.print_emps())


#isinstence and issubclass
print()
print(isinstance(mngr1,Manager))
print(isinstance(mngr1,Employee))
print(isinstance(mngr1,Developer))
print()
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))
print(issubclass(Developer,Employee))