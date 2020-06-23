import timeit


def func_one(count):
    return [str(i) for i in range(count)]


def func_two(count):
    return list(map(str, range(count)))


statement_one = '''
func_one(100)
'''

setup_one = '''
def func_one(count):
    return [str(i) for i in range(count)]
'''

statement_two = '''
func_two(100)
'''

setup_two = '''
def func_two(count):
    return list(map(str, range(count)))
'''

time_took_one = timeit.timeit(statement_one, setup_one, number=1000000)
print(time_took_one)
time_took_two = timeit.timeit(statement_two, setup_two, number=1000000)
print(time_took_two)
