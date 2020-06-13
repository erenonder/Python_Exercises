import time
from datetime import datetime


def add_friend(friend_name, friend_list=[]):
    friend_list.append(friend_name)
    print("friend_list: {}".format(friend_list))


def add_friend_fix(friend_name, friend_list=None):
    if friend_list is None:
        friend_list = []
    friend_list.append(friend_name)
    print("friend_list: {}".format(friend_list))


def print_time(time_to_print=None):
    if time_to_print is None:
        time_to_print = datetime.now()

    print("Printed time: {}".format(time_to_print.strftime('%B %y %A, %H %M %S')))


print(print_time.__defaults__)
print_time()
print(print_time.__defaults__)
time.sleep(3)
print_time(datetime.now())
print(print_time.__defaults__)
time.sleep(3)
print_time()

# my_list = ['Ali', 'Veli']

# print("Defaults: {}".format(add_friend_fix.__defaults__))
# add_friend_fix("Soner")
# print("Defaults: {}".format(add_friend_fix.__defaults__))
# add_friend_fix("Onder", my_list)
# print("Defaults: {}".format(add_friend_fix.__defaults__))
# add_friend_fix("Nihan")
# print("Defaults: {}".format(add_friend_fix.__defaults__))
