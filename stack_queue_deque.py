import unittest

class Stack():

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

class Deque():

    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.append(item)

    def addBack(self, item):
        return self.deque.insert(0, item)

    def removeFront(self):
        return self.deque.pop()

    def removeBack(self):
        return self.deque.pop(0)

    def isEmpty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)


class TestStackQueueDeque(unittest.TestCase):
    def setUp(self):
        # print('Setting up')
        self.stack = Stack()
        self.queue = Queue()
        self.deque = Deque()

    def tearDown(self):
        # print('Tearing Down')
        self.stack = []
        self.queue = []
        self.deque = []

    def test_stacks(self):
        # print('Test Started')
        self.assertEqual(self.stack.isEmpty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.isEmpty(), False)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.isEmpty(), True)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(self.stack.size(), 5)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(self.stack.size(), 5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.size(), 3)
        self.assertEqual(self.stack.isEmpty(), False)

    def test_queues(self):
        self.assertEqual(self.queue.isEmpty(), True)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.isEmpty(), False)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.isEmpty(), True)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.size(), 5)
        self.assertEqual(self.queue.size(), 5)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.isEmpty(), False)

    def test_deque(self):
        self.assertEqual(self.deque.isEmpty(), True)
        self.deque.addFront(1)
        self.assertEqual(self.deque.isEmpty(), False)
        self.deque.addFront(2)
        self.assertEqual(self.deque.removeFront(), 2)
        self.assertEqual(self.deque.size(), 1)
        self.deque.addFront(2)
        self.assertEqual(self.deque.removeBack(), 1)
        self.deque.addBack(1)
        self.assertEqual(self.deque.removeFront(), 2)
        self.assertEqual(self.deque.removeFront(), 1)
        self.assertEqual(self.deque.isEmpty(), True)
        self.deque.addFront('c')
        self.deque.addFront('b')
        self.deque.addFront('a')
        self.deque.addBack(1)
        self.deque.addBack(2)
        self.deque.addBack(3)
        self.assertEqual(self.deque.removeFront(), 'a')
        self.assertEqual(self.deque.removeBack(), 3)
        self.assertEqual(self.deque.removeFront(), 'b')
        self.assertEqual(self.deque.removeFront(), 'c')
        self.assertEqual(self.deque.removeBack(), 2)
        self.assertEqual(self.deque.removeBack(), 1)
        self.assertEqual(self.deque.isEmpty(), True)


if __name__ == '__main__':
    unittest.main()
