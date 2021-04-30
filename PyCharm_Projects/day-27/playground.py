
def add(*args):
    sum = 0
    for elem in args:
        sum += elem

    return sum

def calculate(num, **kwargs):

    result = num

    if "add" in kwargs:
        result += kwargs['add']

    if "mul" in kwargs:
        result *= kwargs['mul']

    return result

# result = add(1, 2, 3, 5, 9)
# print(result)

# res = calculate(6, add=9, mul=5)
# print(res)


class Car:

    def __init__(self, **kwargs):

        self.make = kwargs.get("make", "N/A")
        self.model = kwargs.get("model", "N/A")

        print(f"make: {self.make} model: {self.model}")


my_car = Car(make="BMW")

