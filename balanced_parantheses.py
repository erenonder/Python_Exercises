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

    def __str__(self):
        return str(self.stack)


def balance_check(given_string):
    stack = Stack()
    open_parantheses_set = set('[({')
    closed_parantheses_set = set('])}')
    is_balanced = True

    if len(given_string) % 2 != 0:
        # print(f'Edge Case detected for stack {given_string}')
        is_balanced = False
    else:
        for item in given_string:
            # print(f'item: {item}')
            if item in open_parantheses_set:
                # print('Item in Open Parantheses List')
                stack.push(item)
                # print(f'Push stack: {stack}')
            elif item in closed_parantheses_set:
                # print('Item in Close Parantheses List')
                if stack.isEmpty():
                    # print('stack is Empty')
                    is_balanced = False
                else:
                    inverse_item = stack.pop()
                    # print(f'check_is_inverse item: {item} inverse_item: {inverse_item}')
                    if check_is_inverse(inverse_item, item):
                        pass
                    else:
                        is_balanced = False

        if stack.size() > 0:
            is_balanced = False
    return is_balanced


def check_is_inverse(first, second):
    is_inverse = False
    # print(f'FUNCTION first: {first} second: {second}')
    if first == '[' and second == ']':
        is_inverse = True
    elif first == '(' and second == ')':
        is_inverse = True
    elif first == '{' and second == '}':
        is_inverse = True
    else:
        is_inverse = False

    return is_inverse


class TestBalanceParantheses(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(balance_check('[()]'), True)
        self.assertEqual(balance_check('[()'), False)
        self.assertEqual(balance_check('{'), False)
        self.assertEqual(balance_check('{}'), True)
        self.assertEqual(balance_check('{[()]}'), True)
        self.assertEqual(balance_check('{[()])'), False)
        self.assertEqual(balance_check('[](){([[[]]])}('), False)
        self.assertEqual(balance_check('[{{{(())}}}]((()))'), True)
        self.assertEqual(balance_check('[[[]])]'), False)
        self.assertEqual(balance_check('[](){([[[]]])}'), True)
        self.assertEqual(balance_check('()(){]}'), False)
        self.assertEqual(balance_check('[]'), True)
        self.assertEqual(balance_check('[([{[({([{)])})]}])]'), False)


if __name__ == '__main__':
    unittest.main()
