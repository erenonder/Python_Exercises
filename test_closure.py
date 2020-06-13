# test_closure.py

import unittest
import enclosure
import math


class TestEnclosure(unittest.TestCase):

    def setUp(self):
        # print("Setting up")
        self.test_list = [4, 7, 8]
        self.test_tuple = (9, 5, 8)
        self.test_elem1 = 2
        self.test_elem2 = 9
        self.myfunc_sum = enclosure.map_function(enclosure.operation, self.test_elem1, self.test_elem2, op_name='Sum')
        self.myfunc_sum_list = enclosure.map_function(enclosure.operation, self.test_list, op_name='Sum')
        self.myfunc_sum_mix = enclosure.map_function(enclosure.operation, self.test_list, self.test_elem1, op_name='Sum')

        self.myfunc_mul = enclosure.map_function(enclosure.operation, self.test_elem1, self.test_elem2, op_name='Mul')
        self.myfunc_mul_tuple = enclosure.map_function(enclosure.operation, self.test_tuple, op_name='Mul')
        self.myfunc_mul_mix = enclosure.map_function(enclosure.operation, self.test_tuple, self.test_elem1, op_name='Mul')

    def tearDown(self):
        # print("Tearing Down")
        pass

    def test_enclosure_sum(self):
        self.assertEqual(self.myfunc_sum(), self.test_elem1 + self.test_elem2)

    def test_enclosure_sum_with_list(self):
        self.assertEqual(self.myfunc_sum_list(), sum(self.test_list))

    def test_enclosure_sum_mix(self):
        self.assertEqual(self.myfunc_sum_mix(), sum(self.test_list) + self.test_elem1)

    def test_enclosure_mul(self):
        self.assertEqual(self.myfunc_mul(), self.test_elem1 * self.test_elem2)

    def test_enclosure_mul_with_tuple(self):
        self.assertEqual(self.myfunc_mul_tuple(), math.prod(self.test_tuple))

    def test_enclosure_mul_mix(self):
        self.assertEqual(self.myfunc_mul_mix(), math.prod(self.test_tuple) * self.test_elem1)


if __name__ == "__main__":
    unittest.main()
