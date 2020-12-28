
class Car:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def __str__(self):

        return f"This is a {self.color} car from {self.model}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r},{self.model!r})"

    @classmethod
    def get_class_name(cls):

        print(f'{cls.__name__}')
        # print(f'{self.__class__.__name__}')


myCar = Car('grey', 2018)

print(myCar)

print(repr(myCar))

Car.get_class_name()
