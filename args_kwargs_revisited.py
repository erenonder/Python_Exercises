
def my_func(first_required_arg=3, *args, **kwargs):
    print(
        f'OK first_required_arg: {first_required_arg} args: {args} kwargs: {kwargs}')


my_func(1, 2, 3, fname='Onder', lname='Eren')
