
def my_function(a, b, *args, **kwargs):

    print(a, b)
    print(f'*args: {args}')
    print(f'**kwargs: {kwargs}')

    for arg in args:
        print(f'arg: {arg}')

    for key in kwargs:
        print(f'kwarg[{key}]: {kwargs[key]}')


my_function(1, 2, 3, 4, 5, six=6, seven=7)

my_list = [1, 2, 3, 4, 5]

*begining, end = my_list

print(begining)
