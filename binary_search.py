
import unittest
from random import randint

def binary_search(given_arr, searched_element):

    if len(given_arr) < 1:
        return False
    else:
        mid_index = int(len(given_arr) / 2)
        if given_arr[mid_index] == searched_element:
            return True
        else:
            if given_arr[mid_index] > searched_element:
                return binary_search(given_arr[:mid_index], searched_element)
            else:
                return binary_search(given_arr[mid_index + 1:], searched_element)

class Test_Binary_Search(unittest.TestCase):

    def setUp(self):
        self.number_of_tests = 100
        self.number_of_elements = 20
        self.searched_element = [0] * self.number_of_tests
        self.search_result = [False] * self.number_of_tests

        self.arr_to_search = [[] * self.number_of_elements for i in range(self.number_of_tests)]
        for i in range(self.number_of_tests):
            for j in range(self.number_of_elements):
                random_num = randint(0, 50)
                self.arr_to_search[i].append(random_num)

            self.arr_to_search[i] = sorted(self.arr_to_search[i])
            self.searched_element[i] = randint(0, 10)

            if self.searched_element[i] in self.arr_to_search[i]:
                self.search_result[i] = True

    def tearDown(self):
        self.arr_to_search = []
        self.searched_element = None
        self.search_result = False

    def test_binary_search(self):
        for i in range(self.number_of_tests):
            # print(f'arr_to_search: {self.arr_to_search[i]} searched_element: {self.searched_element[i]} search_result: {self.search_result[i]}')
            self.assertEqual(binary_search(self.arr_to_search[i], self.searched_element[i]), self.search_result[i])


if __name__ == '__main__':

    unittest.main()
