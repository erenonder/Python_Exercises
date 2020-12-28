
# Exercise D1 (30 min)
# Write a decorator which wraps functions to log function
# arguments and the return value on each call. Provide support
# for both positional and named arguments (your wrapper function
# should take both *args and **kwargs and print them both):
def logged(given_func):

    def wrapper(*args, **kwargs):
        print(f"you called {given_func.__name__}{*args, *kwargs.values()}")

        rv = given_func(*args, **kwargs)
        print(f"it returned {rv}")
        return rv

    return wrapper


@ logged
def func(*args):
    return 3 + len(args)


@ logged
def another_function(x, y, z=5):

    return x * y + z


@logged
def some_other_function(*args, **kwargs):

    sum = 0
    for arg in args:
        sum += arg

    for kwarg in kwargs.values():
        sum += kwarg

    return sum


# print(func(4, 4, 4))

# print(another_function(3, 4, 7))

# print(some_other_function(3, 4, 7, x=8))

# Exercise D2 (20 min)
# Write a decorator to cache function invocation results.
# Store pairs arg:result in a dictionary in an attribute of
# the function object. The function being memoized is:
