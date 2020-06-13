import time

def deco_timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        rv = func(*args, **kwargs)
        after = time.time()
        print(f'Time took to run function {func.__name__} is {after-before}')
        return rv
    return wrapper