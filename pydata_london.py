
def adda(x, y):
    'adding two given numbers'
    return x + y


offset = 2
simple_list = [i for i in range(5, 9)]
a = map(lambda x: x + offset, simple_list)

# help(adda)

adda.__doc__ = "Changed help text"
adda.__name__ = "changed_func_name"

# help(adda)

class Adder:

    def __init__(self, offset):
        self.offset = offset

    # def __call__(self, x, y):
    #     return x + y + self.offset

    def sum_with_offset(self, x, y):
        return x + y + self.offset


adder = Adder(2)

# print(adder(3, 5))

# print(adder.sum_with_offset(3, 5))


def another_func():
    rv = 0
    while True:
        yield rv
        rv += 1


# iter_obj = another_func()

# for elem in iter_obj:
#     if elem > 15:
#         break
#     else:
#         print(f'elem: {elem}')


# def iter_func():

#     print('first')
#     yield
#     print('second')
#     yield
#     print('last')
#     yield


# iter_obj = iter_func()

# for _ in iter_obj:
#     pass
