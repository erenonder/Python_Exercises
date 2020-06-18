import math
from math import pi
import random

value = 4.35
print(f"flooring {value} {math.floor(value)} ceiling {math.ceil(value)} rounding {round(value)}")
print(f"logne = {math.log(math.e)}")
print(f"sin of right angle {math.sin(pi/2)}")
print(f"{random.randint(0, 100)}")
random.seed(101)
print('five seeded random')
for i in range(5):
    print(random.randint(0, 100))

mylist = list(range(0, 20))
# mylist2 = [x for x in range(0, 20)]
print(mylist)
for i in range(5):
    print(f"random num from list: {random.choice(mylist)}")

print(random.choices(population=mylist, k=10))  # sample with replacement
print(random.sample(population=mylist, k=10))  # sample without remplacement
random.shuffle(mylist)  # shuffles inplace
print(mylist)
