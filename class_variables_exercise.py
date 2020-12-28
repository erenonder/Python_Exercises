
class MyTest():

    name = 'XXX'
    number = 6

    def __init__(self):
        print('Inited Class')

    def __repr__(self):

        return f"MyTest({self.name}, {self.number})"

    def update_number(self):

        self.number += 1


mytest = MyTest()
# print(repr(mytest))
mytest.update_number()
print(MyTest.number)

print(mytest.number)
