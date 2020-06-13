# from another_file import *
from another_file import Another


class Important(Another):
    def __init__(self):
        super().__init__()


my2obj = Important()
# my2obj.another_func()