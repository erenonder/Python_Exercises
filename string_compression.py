import unittest


def compress_string(given_string):
    string_dict = dict()
    for character in given_string:
        if character in string_dict.keys():
            string_dict[character] += 1
        else:
            string_dict[character] = 1

    compressed_string = ''
    for key in string_dict.keys():
        compressed_string += str(key) + str(string_dict[key])
    # print(string_dict)
    return compressed_string


def unique_chars(given_string):
    unique_str = True
    char_list = sorted(given_string)
    unique_dict = dict()
    for character in char_list:
        if character in unique_dict.keys():
            unique_dict[character] += 1
            unique_str = False
            break
        else:
            unique_dict[character] = 1
    # print(char_list)
    return unique_str


def unique_chars_one_liner(given_string):
    return len(set(given_string)) == len(given_string)


class TestStringCompression(unittest.TestCase):
    def test_string_comp(self):
        self.assertEqual(compress_string(''), '')
        self.assertEqual(compress_string('AABBCC'), 'A2B2C2')
        self.assertEqual(compress_string('AAABCCDDDDD'), 'A3B1C2D5')
        self.assertEqual(compress_string('AAAaaa'), 'A3a3')
        self.assertEqual(compress_string('AAB'), 'A2B1')


class TestStringUniqueness(unittest.TestCase):
    def test_string_uniqueness(self):
        self.assertEqual(unique_chars('abcde'), True)
        self.assertEqual(unique_chars('abca'), False)
        self.assertEqual(unique_chars('x1ytr3'), True)
        self.assertEqual(unique_chars('abcdefge'), False)
        self.assertEqual(unique_chars('abcd123e1ght'), False)
        self.assertEqual(unique_chars(''), True)
        self.assertEqual(unique_chars('goo'), False)
        self.assertEqual(unique_chars('abcdefg'), True)

    def test_string_uniqueness_one_liner(self):
        self.assertEqual(unique_chars_one_liner('abcde'), True)
        self.assertEqual(unique_chars_one_liner('abca'), False)
        self.assertEqual(unique_chars_one_liner('x1ytr3'), True)
        self.assertEqual(unique_chars_one_liner('abcdefge'), False)
        self.assertEqual(unique_chars_one_liner('abcd123e1ght'), False)
        self.assertEqual(unique_chars_one_liner(''), True)
        self.assertEqual(unique_chars_one_liner('goo'), False)
        self.assertEqual(unique_chars_one_liner('abcdefg'), True)


if __name__ == "__main__":
    unittest.main()

compress_string("AAAAABBBBCCC")
