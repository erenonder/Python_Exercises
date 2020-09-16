import unittest
import re

def is_palindrome_with_regex(given_string):

    reg_string = ''.join(re.findall(r'[a-z]+', given_string.lower()))
    return reg_string == reg_string[::-1]

def is_palindrome(given_string):

    palindrome_result = False

    lc_string = given_string.lower()
    pal_list = []
    for letter in lc_string:
        if letter.isalpha():
            pal_list.append(letter)

    for i in range(len(pal_list)):
        if pal_list[i] != pal_list[(i * -1) - 1]:
            break
    else:
        palindrome_result = True

    return palindrome_result


def sort_words(given_string):

    list_string = given_string.split(' ')

    lower_case_list = []
    for word in list_string:
        lower_case_list.append(word.lower())

    lower_case_list.sort()
    final_list = []
    for sorted_word in lower_case_list:
        for word in list_string:
            if sorted_word == word.lower():
                final_list.append(word)

    return ' '.join(final_list)


class TestPalindrome(unittest.TestCase):

    def test_is_palindrome(self):

        self.assertEqual(is_palindrome("Race Car"), True)
        self.assertEqual(is_palindrome("Level"), True)
        self.assertEqual(is_palindrome("Eren"), False)
        self.assertEqual(is_palindrome("Abba"), True)
        self.assertEqual(is_palindrome("Go hang a salami - I'm a lasagna hog"), True)

    def test_is_palindrome_with_regex(self):

        self.assertEqual(is_palindrome_with_regex("Race Car"), True)
        self.assertEqual(is_palindrome_with_regex("Level"), True)
        self.assertEqual(is_palindrome_with_regex("Eren"), False)
        self.assertEqual(is_palindrome_with_regex("Abba"), True)
        self.assertEqual(is_palindrome_with_regex("Go hang a salami - I'm a lasagna hog"), True)

    def test_sort_words(self):
        self.assertEqual(sort_words('banana ORANGE apple'), "apple banana ORANGE")
        self.assertEqual(sort_words('string of Words'), "of string Words")


if __name__ == "__main__":
    unittest.main()
