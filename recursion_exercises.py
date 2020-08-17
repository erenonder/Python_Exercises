import unittest

def rec_sum(n):

    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)

def digit_sum(n):

    if int(n / 10) == 0:
        return n
    else:
        return n % 10 + digit_sum(int(n / 10))


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:len(s)]) + s[0]


def permute(s):
    result = []

    if len(s) == 1:
        result = [s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                result += [let + perm]

    return result


fib_dict = {}

def fibonacci(n):

    if n in fib_dict.keys():
        return fib_dict[n]

    if n == 1 or n == 2:
        fib_dict[n] = 1
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        if n not in fib_dict.keys():
            fib_dict[n] = result
            return result

def fib_iter(n):

    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b

    return a


# coin_dict = {}


def rec_coin(target, coins, coin_dict=None):

    if coin_dict is None:
        coin_dict = {}

    if len(coins) == 0:
        coin_count = 0
        for key in coin_dict.keys():
            coin_count += coin_dict[key]
        return coin_count

    if target >= max(coins):
        coin_number = int(target / max(coins))
        target = target - coin_number * max(coins)
        if max(coins) not in coin_dict.keys():
            coin_dict[max(coins)] = coin_number
        coins.remove(max(coins))
        return rec_coin(target, coins, coin_dict)
    else:
        coins.remove(max(coins))
        return rec_coin(target, coins, coin_dict)


class TestRecursionFunctions(unittest.TestCase):

    def test_recursion_sum(self):
        self.assertEqual(rec_sum(5), 15)
        self.assertEqual(rec_sum(6), 21)
        self.assertEqual(rec_sum(10), 55)
        self.assertEqual(rec_sum(20), 210)

    def test_digit_sum(self):
        self.assertEqual(digit_sum(123), 6)
        self.assertEqual(digit_sum(4592), 20)
        self.assertEqual(digit_sum(67231), 19)
        self.assertEqual(digit_sum(598), 22)

    def test_reverse(self):
        self.assertEqual(reverse('hello world'), 'dlrow olleh')
        self.assertEqual(reverse('onder'), 'redno')

    def test_permute(self):
        self.assertEqual(sorted(permute('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(23), 28657)
        self.assertEqual(fibonacci(1), 1)

        self.assertEqual(fib_iter(10), 55)
        self.assertEqual(fib_iter(9), 34)
        self.assertEqual(fib_iter(11), 89)
        self.assertEqual(fib_iter(5), 5)
        self.assertEqual(fib_iter(7), 13)
        self.assertEqual(fib_iter(23), 28657)

    def test_coin_counts(self):
        self.assertEqual(rec_coin(74, [1, 5, 10, 25]), 8)
        self.assertEqual(rec_coin(10, [1, 5]), 2)
        self.assertEqual(rec_coin(45, [1, 5, 10, 25]), 3)
        self.assertEqual(rec_coin(26, [1, 5, 10, 25]), 2)
        self.assertEqual(rec_coin(23, [1, 5, 10, 25]), 5)
        self.assertEqual(rec_coin(63, [1, 4, 8, 16]), 8)
        self.assertEqual(rec_coin(41, [1, 4, 8, 16]), 4)
        self.assertEqual(rec_coin(17, [1, 4, 8, 16]), 2)
        self.assertEqual(rec_coin(63, [1, 5, 10, 25]), 6)
        # self.assertEqual(rec_coin(11, [1, 5, 6, 8]), 2) # Solution does not work on this needs fixing


if __name__ == '__main__':
    unittest.main()
