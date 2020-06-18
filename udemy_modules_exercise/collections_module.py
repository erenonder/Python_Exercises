from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1, 1, 1, 'a', 'a', 'a', 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
mycountobj = Counter(mylist)
# a dictionary showing how many occurences each key is
print(mycountobj)
# occurences of 'a' key
print(mycountobj['a'])
charcountobj = Counter('aaaabbbbbccccdddeeeeeeeeeee')
print(charcountobj)
print(charcountobj['e'])
# returns most common 2 keys and their values
# as tuple
print(charcountobj.most_common(2))
# returning the number of occurences of the key and removes it
# from the dictionary
print(charcountobj.pop('a'))
print(charcountobj)

# inits non existing keys to a default given value
d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
# this should have returned error if it was
# normal dictionary but instead returns default value
print(d['wrong_key'])

# named tuple is like a class and you can reach the tuple attributes
# as if they are attributes of a class
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
print(Dog)
sammy = Dog(age=5, breed='Husky', name='Sam')
print(sammy.age)
