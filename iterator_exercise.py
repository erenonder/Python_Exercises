import itertools

# counter = itertools.count(start=5, step=5)

on_off = ('On', 'Off')
counter = itertools.cycle(on_off)

# print(pow(5, 2))

squares = map(pow, range(10), itertools.repeat(2))

print(list(squares))

letters = ['a', 'b', 'c', 'd']

# result = itertools.combinations(letters, 2)
result = itertools.permutations(letters, 2)
for item in result:
    print(item)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

data = [100, 200, 300, 400]

daily_data = list(itertools.zip_longest(range(10), data))

print(daily_data)
