import unittest
import random
from time import time

def check_prime(number):

    prime_number = True
    for i in range(2, int(number / 2) + 1):
        if number % i == 0 and number != i and number != 2:
            prime_number = False
            break
        else:
            continue

    return prime_number


def get_prime_factors(number):

    prime_factors = []
    if check_prime(number):
        prime_factors.append(number)
    else:
        for i in range(2, int(number / 2) + 1):
            if check_prime(i) and number % i == 0:
                prime_factors.append(i)
                check_number = number / i
                while check_number % i == 0:  # check if there are more occurences of this prime
                    prime_factors.append(i)
                    check_number = check_number / i

                # test here if we have the whole list already
                multiplication = 1
                for item in prime_factors:
                    multiplication *= item

                # if this condition is satisfied we have the whole list
                if multiplication == number:
                    break

    return prime_factors


class TestPrime(unittest.TestCase):

    def test_check_prime(self):

        self.assertFalse(check_prime(15))
        self.assertFalse(check_prime(16))
        self.assertFalse(check_prime(18))
        self.assertFalse(check_prime(27))
        self.assertFalse(check_prime(33))
        self.assertFalse(check_prime(45))
        self.assertFalse(check_prime(39))
        self.assertTrue(check_prime(2))
        self.assertTrue(check_prime(3))
        self.assertTrue(check_prime(5))
        self.assertTrue(check_prime(7))
        self.assertTrue(check_prime(11))
        self.assertTrue(check_prime(13))
        self.assertTrue(check_prime(17))
        self.assertTrue(check_prime(19))
        self.assertTrue(check_prime(23))
        self.assertTrue(check_prime(29))
        self.assertTrue(check_prime(179))
        self.assertTrue(check_prime(709))
        self.assertTrue(check_prime(1223))
        self.assertTrue(check_prime(1847))
        self.assertTrue(check_prime(6143))
        self.assertTrue(check_prime(5953))

    def test_prime_factors(self):
        test_count = 1000

        # start_time = time()
        for i in range(test_count):
            number_to_check = random.randint(1, 1000)
            prime_factors_list = get_prime_factors(number_to_check)
            multiplication_result = 1
            for prime in prime_factors_list:
                self.assertTrue(check_prime(prime))
                multiplication_result *= prime

            self.assertEqual(number_to_check, multiplication_result)
            with open('get_primes_test.txt', 'a') as prime_file:
                prime_file.write(
                    f'Prime factors of {number_to_check} is {prime_factors_list} and the multiplication of the list is {multiplication_result}\n')

        # end_time = time()
        # print(f'Test took {end_time - start_time} seconds')


if __name__ == '__main__':
    unittest.main()
