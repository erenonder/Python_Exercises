
import unittest
import random


def maximize_profit(price_list):
    max_profit = 0
    for index, price in enumerate(price_list):
        if index != len(price_list) - 1:
            max_price = max(price_list[index + 1:])
            if max_price - price > max_profit:
                max_profit = max_price - price
        else:
            return max_profit

def maximize_profit_greedy(price_list):

    max_profit = 0
    min_price = price_list[0]

    for price in price_list:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(profit, max_profit)

    return max_profit


def multiplication_list(mul_list):
    result_list = []
    for index, elem in enumerate(mul_list):
        result = 1
        for num_index, num in enumerate(mul_list):
            if index != num_index:
                result *= num
        result_list.append(result)
    return result_list

def calc_overlap(m1, dim1, m2, dim2):

    i_start = max(m1, m2)

    i_end = min(m1 + dim1, m2 + dim2)

    if i_start >= i_end:
        return (None, None)
    else:
        return (i_start, i_end)


def check_overlap(first_rect, second_rect):
    intersection_dict = {}
    intersection_x = calc_overlap(rect_1['x'], rect_1['w'], rect_2['x'], rect_2['w'])
    intersection_y = calc_overlap(rect_1['y'], rect_1['h'], rect_2['y'], rect_2['h'])
    print(f'intersection_x: {intersection_x}')
    print(f'intersection_y: {intersection_y}')

    if intersection_x == (None, None) or intersection_y == (None, None):
        print('No intersection')
    else:
        intersection_dict['x1'] = intersection_x[0]
        intersection_dict['x2'] = intersection_x[1]
        intersection_dict['y1'] = intersection_y[0]
        intersection_dict['y2'] = intersection_y[1]
        return intersection_dict


# rect_1 = {'x': 2, 'y': 4, 'w': 5, 'h': 12}
# rect_2 = {'x': 3, 'y': 5, 'w': 7, 'h': 18}

# resulting_rect = check_overlap(rect_1, rect_2)
# print(f'resulting_rect: {resulting_rect}')

def inverse_string(given_string):
    # print(f'{given_string}')
    if len(given_string) <= 1:
        return given_string
    else:
        return inverse_string(given_string[1:]) + given_string[0]


def square_root(number):

    if number == 0:
        return ValueError
    if number == 1:
        return 1

    for k in range(number / 2 + 1):
        if number < k**2:
            return k - 1
        elif k**2 == number:
            return number

    return k


def remove_duplicate_chars(given_sting):
    char_list = []
    for elem in given_sting:
        if elem not in char_list:
            char_list.append(elem)

    my_str = ''.join(char_list)
    return my_str

def is_sum_of_two(given_list, target):
    my_set = set()
    for elem in given_list:
        need = target - elem

        if need in my_set:
            return True
        else:
            my_set.add(elem)

    return False


def unique_id(given_list):

    unique_id = 0

    for elem in given_list:
        print(f'elem: {elem} unique_id: {unique_id}')
        unique_id ^= elem
        print(f'unique_id: {unique_id}')

check_list = [1, 2, 6, 2, 1]
res = unique_id(check_list)
# print(f'unique: {res}')


class TestProfit(unittest.TestCase):

    def test_maximize_profit(self):
        price_list = [12, 11, 15, 3, 10]
        self.assertEqual(maximize_profit(price_list), 7)
        self.assertEqual(maximize_profit_greedy(price_list), 7)

        price_list = [3, 9, 7, 12, 4]
        self.assertEqual(maximize_profit(price_list), 9)
        self.assertEqual(maximize_profit_greedy(price_list), 9)

        price_list = [12, 7, 41, 40, 45]
        self.assertEqual(maximize_profit(price_list), 38)
        self.assertEqual(maximize_profit_greedy(price_list), 38)

        price_list = [3, 4, 5, 9, 34]
        self.assertEqual(maximize_profit(price_list), 31)
        self.assertEqual(maximize_profit_greedy(price_list), 31)

        price_list = [3, 23, 24, 8, 21]
        self.assertEqual(maximize_profit(price_list), 21)
        self.assertEqual(maximize_profit_greedy(price_list), 21)

        price_list = [7, 21, 2, 3, 41]
        self.assertEqual(maximize_profit(price_list), 39)
        self.assertEqual(maximize_profit_greedy(price_list), 39)


if __name__ == '__main__':

    unittest.main()
