# enclosure.py

def map_function(call_func, *args, **kwargs):
    # print('onder args: {} kwargs: {}'.format(args, kwargs))

    def inner_func():
        result = call_func(*args, **kwargs)
        return result
    return inner_func


def operation(*args, **kwargs):
    suma = 0
    mult = 1
    res = 0
    if kwargs['op_name'] == 'Sum':
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for elem in arg:
                    suma += elem
            else:
                suma += arg
        res = suma
    elif kwargs['op_name'] == 'Mul':
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for elem in arg:
                    mult *= elem
            else:
                mult *= arg
        res = mult
    return res


if __name__ == '__main__':
    myfunc = map_function(operation, [6, 7], 5, op_name='Sum', sub_op_name='Normal')
    print(myfunc())
