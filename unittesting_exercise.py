import unittest


class MyException(Exception):

    pass

class Operations:

    def divider_function(self, f_num, s_num):

        try:
            return f_num / s_num
        except ZeroDivisionError:
            raise MyException("Second Number is zero")

    def my_generator(self, lim):

        mylist = [i for i in range(lim**2)]

        list_len = len(mylist)
        # print("Length: {}".format(list_len))

        for i in range(list_len):
            yield mylist[(list_len - 1) - i]

class MyTestClass(unittest.TestCase):

    def setUp(self):
        self.class_on_test = Operations()
        # print("Setting Up...")

    def tearDown(self):
        # print("Tearing Down...")
        pass

    def test_division(self):

        self.assertEqual(self.class_on_test.divider_function(4, 2), 2)

        with self.assertRaises(MyException):

            self.class_on_test.divider_function(3, 0)

    def test_generator(self):

        my_num = 5
        gen = self.class_on_test.my_generator(my_num)

        self.assertEqual(next(gen), my_num**2 - 1)
        self.assertEqual(next(gen), my_num**2 - 2)
        self.assertEqual(next(gen), my_num**2 - 3)

        for i, index in enumerate(gen):
            self.assertEqual(i, my_num**2 - 4 - index)


if __name__ == '__main__':
    # op = Operations()

    # gen = op.my_generator(5)

    # print(gen.__next__())
    # print(gen.__next__())
    # print(gen.__next__())
    # print(gen.__next__())

    unittest.main()
