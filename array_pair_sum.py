import unittest


def pair_sum(arr, k):
    unique_pair_count = 0
    # print(f'Given array {arr}')
    pairs_list = []
    unique_pair_list = []
    for elem in arr:
        needed_elem = k - elem
        if needed_elem in arr:
            pairs_list.append([elem, needed_elem])

    for pair in pairs_list:
        reversed_pair = list(reversed(pair))
        if pair not in unique_pair_list and reversed_pair not in unique_pair_list:
            unique_pair_list.append(pair)
            unique_pair_count += 1

    return unique_pair_count


def pair_sum_with_set(arr, k):
    pairs_set = set()

    for elem in arr:
        needed_elem = k - elem
        if needed_elem in arr:
            pairs_set.add((min(elem, needed_elem), max(elem, needed_elem)))

    return len(pairs_set)

class TestPairSum(unittest.TestCase):

    def test_pair_sum(self):
        self.assertEqual(pair_sum([1, 3, 2, 2], 4), 2)
        self.assertEqual(pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        self.assertEqual(pair_sum([1, 2, 3, 1], 3), 1)

    def test_pair_sum_with_set(self):
        self.assertEqual(pair_sum_with_set([1, 3, 2, 2], 4), 2)
        self.assertEqual(pair_sum_with_set([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        self.assertEqual(pair_sum_with_set([1, 2, 3, 1], 3), 1)


if __name__ == '__main__':
    unittest.main()
