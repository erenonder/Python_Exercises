
class ContextMan:

    def __init__(self, file_name, open_mode):
        self.file = open(file_name, open_mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()


with ContextMan('onder.txt', 'w') as cm:
    cm.write('I am writing')


class Gen:

    def __init__(self, limit):

        self.limit = limit
        self.start = 0

    def __next__(self):

        if self.start == self.limit:
            raise StopIteration()
        else:
            result = self.start**2
            self.start += 1
            return result


def gen_func(limit):
    for i in range(limit):
        yield i**2


gen_obj = Gen(5)

print('Generator function output')
gen_f = gen_func(5)
for i in gen_f:
    print(f'{i}')

print('Generator class output')
try:
    for i in range(10):
        print(next(gen_obj))
except StopIteration:
    print('Iteration Stoped')
