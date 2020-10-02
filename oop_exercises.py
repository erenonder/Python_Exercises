

class Employee:

    raise_amount = 1.04
    employee_count = 0

    def __init__(self, first, last='Eren', pay=60000):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + "@company.com"

        Employee.employee_count += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __str__(self):
        return f'Name: {self.first}\nSurname: {self.last}\nEmail: {self.email}\nPay: {self.pay}'


emp_1 = Employee('Onder', pay=50000)
emp_2 = Employee('Nihan', last='Ocak')

# print(emp_2.fullname())
# print(Employee.fullname(emp_1))
# print(emp_2)

# print(Employee.employee_count)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
