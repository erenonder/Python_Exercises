# generators.py

from decorators import deco_timer


@deco_timer
def compute():
    mylist = []
    for i in range(100000):
        mylist.append(i)
    return mylist


newlist = compute()


@deco_timer
def gen_compute():
    for i in range(100000):
        yield i


newgen = gen_compute()

