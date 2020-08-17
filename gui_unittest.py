
import unittest
from gui_to_test import *
import threading
import argparse
import sys

my_gui = None

class TestGUI(unittest.TestCase):

    def test_case_1(self):
        label_text = my_gui.label.cget('text')
        self.assertEqual(label_text, "This is our first GUI!")

    def test_case_2(self):
        my_gui.greet_button.invoke()
        self.assertEqual(True, True)

    def test_case_onder(self):
        my_gui.close_button.invoke()
        self.assertEqual(3 + 5, 8)


def parse_arguments(args):

    parser = argparse.ArgumentParser()
    parser.add_argument("-x", help="item for test")
    return parser.parse_args(args)


def start_test():
    for i in range(len(sys.argv) - 1):
        sys.argv.pop()
        # print(popped)
    unittest.main()


if __name__ == "__main__":
    parser = parse_arguments(sys.argv[1:])
    # print(f'Onder {parser.x}')
    t = threading.Timer(2.0, start_test)
    t.start()
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
