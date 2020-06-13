# tips_and_tricks.py

# ternary
condition = False

x = 1 if condition else 0

print(x)

# large numbers

large_num = 100_000_000
print(f'{large_num:,}')

# context manager
with open('sample.txt') as f:
    file_content = f.read()

words = file_content.split()
print(len(words))

# enumarate

names = ['Onder', 'Soner', 'Nihan']

for index, name in enumerate(names, start=1):
    print(index, name)

# zipping

names = ['Peter', 'Clark', 'Wade', 'Bruce']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for name, hero in zip(names, heroes):
    print(f'{hero} --> {name}')

# unpacking
a, _ = (1, 2)
print(a)

a, b, *c = [1, 2, 3, 4, 5]
print(a, b)
print(c)


# set and get attribute
class Person():
    pass


person = Person()

person_info = {'first': 'Onder', 'last': 'Eren'}

for key, val in person_info.items():
    setattr(person, key, val)

for key in person_info.keys():
    val = getattr(person, key)
    print(val)
