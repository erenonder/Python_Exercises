import functools


def trace(func):
    # This avoids missing the wrapped function's metadata
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f'TRACE: Calling function {func.__name__} with arguments {args}, {kwargs}')
        rv = func(*args, **kwargs)
        print(f'TRACE: {func.__name__} returned {rv}')
        return rv

    return wrapper


@trace
def my_sample_function(*args, **kwargs):
    'This is a function which multiplies the arguments given'
    result = 1
    for elem in args:
        result *= elem

    for elem in kwargs.values():
        result *= elem

    return result


# my_sample_function = trace(my_sample_function)
return_val = my_sample_function(1, 2, arg_third=3)
print(return_val)
print(my_sample_function.__name__)
print(my_sample_function.__doc__)
