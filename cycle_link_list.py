import unittest

class Node():

    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check(node):
    circular_list = False
    initial_node = node

    while node.next_node is not None:
        if node.next_node == initial_node:
            circular_list = True
            break
        else:
            node = node.next_node

    return circular_list


def reverse(head):
    prev_node = None
    next_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next_node

        current_node.next_node = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


def nth_to_the_last_node(position, head):
    node = head
    number_of_nodes = 1
    while node.next_node is not None:
        number_of_nodes += 1
        node = node.next_node

    node_count = number_of_nodes - position

    node = head
    for i in range(node_count):
        node = node.next_node

    return node


def nth_to_the_last_node_better_solution(position, head):
    right_node = head
    left_node = head

    for i in range(position - 1):
        if right_node.next_node is None:
            raise LookupError(f'{position} is bigger than number of elements')
        right_node = right_node.next_node

    while right_node.next_node is not None:
        left_node = left_node.next_node
        right_node = right_node.next_node

    return left_node


class TestCircularLinkList(unittest.TestCase):

    def setUp(self):
        self.a = Node(1)
        self.b = Node(2)
        self.c = Node(3)
        self.d = Node(4)
        self.e = Node(5)

    def tearDown(self):
        del self.a
        del self.b
        del self.c
        del self.d
        del self.e

    def test_circulation_1(self):
        self.a.next_node = self.b
        self.b.next_node = self.c
        self.c.next_node = self.d
        self.d.next_node = self.a

        self.assertEqual(cycle_check(self.b), True)
        self.assertEqual(cycle_check(self.a), True)
        self.assertEqual(cycle_check(self.c), True)
        self.assertEqual(cycle_check(self.d), True)

    def test_circulation_2(self):
        self.a.next_node = self.b
        self.b.next_node = self.c
        self.c.next_node = self.d

        self.assertEqual(cycle_check(self.b), False)
        self.assertEqual(cycle_check(self.a), False)
        self.assertEqual(cycle_check(self.c), False)
        self.assertEqual(cycle_check(self.d), False)

    def test_reversal(self):
        self.a.next_node = self.b
        self.b.next_node = self.c
        self.c.next_node = self.d

        self.assertEqual(reverse(self.a), self.d)
        self.assertEqual(self.d.next_node, self.c)
        self.assertEqual(self.c.next_node, self.b)
        self.assertEqual(self.b.next_node, self.a)

    def test_nth_node(self):
        self.a.next_node = self.b
        self.b.next_node = self.c
        self.c.next_node = self.d
        self.d.next_node = self.e

        self.assertEqual(nth_to_the_last_node(2, self.a), self.d)
        self.assertEqual(nth_to_the_last_node(1, self.a), self.e)
        self.assertEqual(nth_to_the_last_node(3, self.a), self.c)
        self.assertEqual(nth_to_the_last_node(4, self.a), self.b)
        self.assertEqual(nth_to_the_last_node(5, self.a), self.a)

    def test_nth_node_better_solution(self):
        self.a.next_node = self.b
        self.b.next_node = self.c
        self.c.next_node = self.d
        self.d.next_node = self.e

        self.assertEqual(nth_to_the_last_node_better_solution(2, self.a), self.d)
        self.assertEqual(nth_to_the_last_node_better_solution(1, self.a), self.e)
        self.assertEqual(nth_to_the_last_node_better_solution(3, self.a), self.c)
        self.assertEqual(nth_to_the_last_node_better_solution(4, self.a), self.b)
        self.assertEqual(nth_to_the_last_node_better_solution(5, self.a), self.a)

        with self.assertRaises(LookupError):
            nth_to_the_last_node_better_solution(6, self.a)


if __name__ == '__main__':
    unittest.main()



