# oop_try.py

class Employee():

    raise_amt = 1.04

    def __init__(self, name, lname, pay):
        self.name = name
        self.lname = lname
        self.pay = pay

    @classmethod
    def from_string(cls, str):
        fname, sname, pay = str.split('-')
        return cls(fname, sname, float(pay))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print('Not a workday go home')
            return False
        print('Yes a workday start working now')
        return True

# myobj = Employee.from_string('Onder-Eren-37000')
myobj = Employee('Onder', 'Eren', 37000)

# myobj.raise_amt = 1.05

print(myobj.raise_amt)
myobj.apply_raise()
print(myobj.pay)

import datetime

my_date = datetime.date(2020, 10, 4)

Employee.is_workday(my_date)


