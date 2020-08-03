import unittest

class Queue2Stacks():

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):

        # FILL OUT CODE HERE
        while len(self.stack2) > 0:
            stack_2_element = self.stack2.pop()
            self.stack1.append(stack_2_element)

        self.stack1.append(element)

    def dequeue(self):

        # FILL OUT CODE HERE
        while len(self.stack1) > 0:
            element = self.stack1.pop()
            self.stack2.append(element)

        return self.stack2.pop()

    def peek(self):
        while self.stack1 != []:
            element = self.stack1.pop()
            print(f'Stack1: {element}')

        while len(self.stack2) > 0:
            element = self.stack2.pop()
            print(f'Stack2: {element}')


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue2Stacks()

    def tearDown(self):
        del self.queue

    def test_queue_with_stacks(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)

        with self.assertRaises(IndexError):
            self.queue.dequeue()

        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.assertEqual(self.queue.dequeue(), 'a')
        self.queue.enqueue('c')
        self.queue.enqueue('d')
        self.assertEqual(self.queue.dequeue(), 'b')
        self.assertEqual(self.queue.dequeue(), 'c')
        self.assertEqual(self.queue.dequeue(), 'd')

        # self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_recursive(self):
        for i in range(5):
            self.queue.enqueue(i)

        for i in range(5):
            self.assertEqual(self.queue.dequeue(), i)


if __name__ == "__main__":
    unittest.main()
