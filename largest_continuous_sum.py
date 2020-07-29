import unittest


def large_cont_sum(arr):
    max_sum = 0
    saved_sum = 0
    sum_dict = dict()
    start_index = 0

    while start_index < len(arr):
        for elem in arr[start_index:]:
            if start_index < len(arr):
                max_sum += elem
                if max_sum > saved_sum:
                    saved_sum = max_sum
                    sum_dict[start_index] = saved_sum
        start_index += 1
        max_sum = 0
        saved_sum = 0

    return max(sum_dict.values())

def large_cont_sum_instructor_solution(arr):

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)

        max_sum = max(current_sum, max_sum)

    return max_sum


class TestLargestContinuousSum(unittest.TestCase):
    def test_largest_cont_sum(self):
        self.assertEqual(large_cont_sum([1, -2, 4, -4, 7]), 7)
        self.assertEqual(large_cont_sum([1, 2, 3, 4, 7]), 17)
        self.assertEqual(large_cont_sum([1, 2, -4, 4, 7]), 11)
        self.assertEqual(large_cont_sum([-1, 2, -1, 4, 7]), 12)
        self.assertEqual(large_cont_sum([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(large_cont_sum([-1, 1]), 1)

    def test_largest_cont_sum_instructor(self):
        self.assertEqual(large_cont_sum_instructor_solution([1, -2, 4, -4, 7]), 7)
        self.assertEqual(large_cont_sum_instructor_solution([1, 2, 3, 4, 7]), 17)
        self.assertEqual(large_cont_sum_instructor_solution([1, 2, -4, 4, 7]), 11)
        self.assertEqual(large_cont_sum_instructor_solution([-1, 2, -1, 4, 7]), 12)
        self.assertEqual(large_cont_sum_instructor_solution([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(large_cont_sum_instructor_solution([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(large_cont_sum_instructor_solution([-1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
