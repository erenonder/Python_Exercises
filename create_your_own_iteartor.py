# create_your_own_iteartor.py

class PowerOfTwo:

    def __init__(self, max_count):
        # print('Init method of PowerOfTwo class')
        self.max_count = max_count
        self.cur_index = 0

    def __iter__(self):
        # print('Iter method of PowerOfTwo class')
        return self

    def __next__(self):
        # print('Next method of PowerOfTwo class')
        if self.cur_index > self.max_count:
            raise StopIteration
        index = self.cur_index
        self.cur_index += 1
        return 2**index


# print('Before Creating PowerOfTwo object')
my_obj = PowerOfTwo(7)
# print('After Creating PowerOfTwo object')

count = 0
for iter_obj in my_obj:
    print(f"Class {count}. power of two is: {iter_obj}")
    count += 1


def poweroftwo(max_count):
    print('Start Gen Function')
    for i in range(max_count + 1):
        yield (i, 2**i)
    print('End Gen Function')


for elem, res in poweroftwo(7):
    print(f'Function {elem}. power of two is: {res}')


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


# my_sentence = Sentence('This is a test')

# for word in my_sentence:
#     print(word)


def gen_word(sentence):
    for word in sentence.split():
        yield word


my_sentence = gen_word('This is a test')

for word in my_sentence:
    print(word)
