

def fib(elem):

    a, b = 0, 1

    for _ in range(elem):

        a, b = b, a + b
        yield a


def mygen():

    for i in range(10):
        yield i

# genobj = fib(1000000)


for elem in fib(15):
    a = elem
    print(f'{a} ', end="")

print('\n') 
# print(next(genobj))

# print(next(genobj))
# print(next(genobj))

# for x in genobj:
    # print(x)