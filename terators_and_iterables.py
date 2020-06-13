# iterators_and_iterables.py

# nums = [1, 2, 3]

# i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))
# for num in nums:
#     print(num)

# while True:
#     try:
#         elem = next(i_nums)
#         print(elem)
#     except StopIteration:
#         break

class MyRange:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration


def myrange_gen(start, stop, step):

    while start < stop:
        value = start
        start += step
        yield value


myrange_func = myrange_gen(1, 23, 4)

for i in myrange_func:
    print(i)

# myrange = MyRange(1, 7, 2)

# for i in myrange:
#     print(i)
