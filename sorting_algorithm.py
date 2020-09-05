import random
import unittest


def bubble_sort(arr):
    phase = 0
    # count = 0
    for n in range(len(arr) - 1):
        for index in range(len(arr) - 1 - n):
            # count += 1
            if arr[index] > arr[index + 1]:
                temp = arr[index + 1]
                arr[index + 1] = arr[index]
                arr[index] = temp
                phase += 1
                # print(f'phase {phase}: arr: {arr} count: {count}')

def selection_sort(arr):

    for n in range(len(arr) - 1):
        for index in range(n + 1, len(arr)):
            if arr[n] > arr[index]:
                temp = arr[n]
                arr[n] = arr[index]
                arr[index] = temp


def insertion_sort(arr):

    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:

            arr[position] = arr[position - 1]
            arr[position - 1] = current_value
            position = position - 1

        arr[position] = current_value

class TestSorting(unittest.TestCase):

    def setUp(self):
        self.given_arr = []

        for n in range(20):
            num = random.randint(0, 50)
            if num not in self.given_arr:
                self.given_arr.append(num)

        self.copy_given_array = self.given_arr.copy()

    def tearDown(self):
        self.given_arr = []
        self.copy_given_array = []

    def test_buble_sort(self):

        bubble_sort(self.given_arr)

        self.assertEqual(len(self.given_arr), len(self.copy_given_array))
        self.assertEqual(self.given_arr, sorted(self.copy_given_array))
        # print(f'sorted arr: {self.given_arr} initial array: {self.copy_given_array}')

    def test_selection_sort(self):
        selection_sort(self.given_arr)

        self.assertEqual(len(self.given_arr), len(self.copy_given_array))
        self.assertEqual(self.given_arr, sorted(self.copy_given_array))
        # print(f'sorted arr: {self.given_arr} initial array: {self.copy_given_array}')

    def test_insertion_sort(self):
        insertion_sort(self.given_arr)

        self.assertEqual(len(self.given_arr), len(self.copy_given_array))
        self.assertEqual(self.given_arr, sorted(self.copy_given_array))
        # print(f'sorted arr: {self.given_arr} initial array: {self.copy_given_array}')


if __name__ == '__main__':
    unittest.main()
