
class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


def reverse_the_string(given_string):
    """
    #Returns the reversed String.

    #Parameters:
    #    given_string:The string which is to be reversed.

    #Returns:
    #    reversed_string:The string which gets reversed.
    """
    return given_string[::-1]


# print(reverse_the_string("onder"))

print("String from calling doc")
print(reverse_the_string.__doc__)
print("String from calling help")
help(reverse_the_string)


def check_divisible_by(x, y):
    '''
    This function checks if the
    first given number is
    divisible by the second given number
    '''

    divisible_by_this_num = False
    if x % y == 0:
        divisible_by_this_num = True

    return divisible_by_this_num


print(check_divisible_by(9, 3))

print(check_divisible_by.__doc__)

mycls = ClassName(4)
print(mycls.__doc__)
