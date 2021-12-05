
def filter_list(list_to_filter):
    new_list = list()
    for elem in list_to_filter:
        if not isinstance(elem, str):
            new_list.append(elem)

    return new_list


def find_outlier(integers):
    outlier = list()
    outlier_even = True
    even_count = 0
    odd_count = 0
    for elem in integers:
        if elem % 2 == 0 and even_count != 2:
            even_count += 1
            if even_count == 2:
                outlier_even = False
            outlier.append(elem)
        elif elem % 2 != 0 and odd_count != 2:
            odd_count += 1
            outlier.append(elem)

        if len(outlier) == 3:
            break

    print(f"Final List: {outlier} outlier_even: {outlier_even}")
    for elem in outlier:
        if outlier_even:
            if elem % 2 == 0:
                return elem
        else:
            if elem % 2 != 0:
                return elem

    return outlier


def iq_test(numbers):
    numbers_list = numbers.split()
    numbers = [int(i) for i in numbers_list]
    # print(numbers)

    outlier = dict()
    outlier_even = True
    even_count = 0
    odd_count = 0
    for elem in numbers:
        if elem % 2 == 0 and even_count != 2:
            even_count += 1
            if even_count == 2:
                outlier_even = False
            outlier[elem] = numbers.index(elem)
        elif elem % 2 != 0 and odd_count != 2:
            odd_count += 1
            outlier[elem] = numbers.index(elem)

        if len(outlier) == 3:
            break

    # print(f"Final List: {outlier} outlier_even: {outlier_even}")
    for elem in outlier:
        if outlier_even:
            if elem % 2 == 0:
                outlier_elem = elem
        else:
            if elem % 2 != 0:
                outlier_elem = elem

    index_of_outlier = outlier[outlier_elem]
    return index_of_outlier + 1


def accum(s):
    accumulated_string = ""
    for index, char in enumerate(s):
        print(f"index: {index} lens: {len(s)}")
        new_chain = char * (index + 1)
        accumulated_string += new_chain.title()

        if (index + 1) != len(s):
            accumulated_string += '-'

    return accumulated_string


def is_prime(num):
    if num < 2:
        return False
    else:
        i = 2

        while i**2 <= num:
            if num % i == 0:
                return False

            i += 1

        return True


def count_bits(n):
    one_count = 0
    while n > 0:
        if n % 2 != 0:
            one_count += 1
        n = int(n / 2)

    return one_count


def solution(s):
    newlist = [letter for letter in s]
    final_list = list()

    try:
        for i in range(0, len(newlist), 2):
            final_list.append(newlist[i] + newlist[i + 1])
    except IndexError as msg:
        final_list.append(newlist[i] + "_")

    return final_list


def rot13(message):

    new_str = ""
    for letter in message:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            new_letter_num = ord(letter) + 13

            if new_letter_num > ord('z'):
                new_letter_num -= 26
            new_str += chr(new_letter_num)
        elif ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            new_letter_num = ord(letter) + 13
            if new_letter_num > ord('Z'):
                new_letter_num -= 26
            new_str += chr(new_letter_num)
        else:
            new_str += letter

    return new_str


rot13("test")  # "grfg"
rot13("Test")  # "Grfg"
