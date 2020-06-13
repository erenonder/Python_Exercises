
from decorators import deco_timer
import time

@deco_timer
def add(*args, **kwargs):
    sum = 0
    print(f'these are keyword argumens {kwargs}')
    for i in kwargs:
        print(f'key: {i} value: {kwargs[i]}')
    for i in args:
        sum += i
        time.sleep(1)
    print(f"sum of {args} is {sum}")

add(3,5,8, 11, sleep_time = 1, def_argument = 9)