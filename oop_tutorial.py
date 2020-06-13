import datetime


class Employee():
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_employees += 1

    @property
    def email(self):
        return f"{self.fname.lower()}.{self.lname.lower()}@email.com"

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self, fullname):
        self.fname, self.lname = fullname.split(' ')

    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.lname = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        # print(f"{fname} {lname} {pay}")
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __repr__(self):
        return f"Employee({self.fname}, {self.lname}, {self.pay})"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)

        if employees is None:
            self.employess = []
        else:
            self.employees = employees

    def add_employee(self, new_emp):
        if new_emp not in self.employees:
            self.employees.append(new_emp)

    def rem_employee(self, old_emp):
        if old_emp in self.employees:
            self.employees.remove(old_emp)

    def show_employees(self):
        print("Manager's Employees")
        for emp in self.employees:
            print(f"{emp.fullname()}")
        print("-------------------")


dev1 = Developer("Onder", "Eren", 50000, "Python")
emp1 = Employee("Nihan", "Ocak", 60000)
man1 = Manager("Elon", "Musk", 9000000, [dev1, emp1])

# man1.show_employees()

emp3_str = 'Jane-Doe-90000'

emp3 = Employee.from_string(emp3_str)

emp3.fullname = "Jim Hendrix"
print(emp3.email)
print(emp3.fullname)

# del emp3.fullname

# print(emp3.fullname)

# man1.rem_employee(dev1)

# man1.show_employees()

# print(isinstance(dev1, Manager))
# print(issubclass(Manager, Developer))

# print(emp1 + dev1)
# print(len(emp1))
# date_check = datetime.date(2020, 5, 25)

# print(Employee.is_workday(date_check))

# print(Employee.num_of_employees)
# print(dev1.prog_lang)
# print(dev1.email)

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
