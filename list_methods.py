import random


def gensquares(N):
    for i in range(N):
        yield i**2


# for x in gensquares(10):
#     print(x)

mylist = []


def rand_num(low, high, count):
    for i in range(count):
        yield random.randint(low, high)


for num in rand_num(1, 100, 5):
    mylist.append(num)

print(mylist)

gencomp = (elem**2 for elem in mylist if elem < 10)

for item in gencomp:
    print(item)
else:
    print('No items')


def find_index(list_search, search_elems):
    found = False
    for index, elem in enumerate(list_search):
        for i in search_elems:
            if i == elem:
                val = index
                found = True
                break
        if found:
            break
    else:
        return -1
    return val


search_elems = [x for x in range(10)]

print(f'The item {search_elems} you search in list {mylist} is at index {find_index(mylist, search_elems)}')
