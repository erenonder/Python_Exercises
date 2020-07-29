import unittest


def find_missing_element(first_array, second_array):
    first_dict = dict()

    for element in first_array:
        if element in first_dict.keys():
            first_dict[element] += 1
        else:
            first_dict[element] = 1

    for element in second_array:
        if element in first_dict.keys():
            first_dict[element] -= 1

    for key in first_dict.keys():
        if first_dict[key] > 0:
            missing_element = key

    return missing_element


def instructor_solution(first_array, second_array):
    second_dict = dict()

    for element in second_array:
        if element in second_dict.keys():
            second_dict[element] += 1
        else:
            second_dict[element] = 1

    for element in first_array:
        if element in second_dict.keys():
            second_dict[element] -= 1
            if second_dict[element] < 0:
                missing_element = element
        else:
            missing_element = element

    return missing_element


def find_missing_element_with_zip(first_array, second_array):
    first_array.sort()
    second_array.sort()

    for num1, num2 in zip(first_array, second_array):
        if num1 != num2:
            return num1

    return first_array[-1]


class TestMissingElement(unittest.TestCase):

    def test_missing_element(self):
        self.assertEqual(find_missing_element([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(find_missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(find_missing_element([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)

    def test_missing_element_with_zip(self):
        self.assertEqual(find_missing_element_with_zip([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(find_missing_element_with_zip([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(find_missing_element_with_zip([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)

    def test_instructor_solution(self):
        self.assertEqual(instructor_solution([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(instructor_solution([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(instructor_solution([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)


if __name__ == "__main__":
    unittest.main()
