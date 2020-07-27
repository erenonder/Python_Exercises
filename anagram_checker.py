import unittest


def easier_anagram_check(s1, s2):
    is_anagram = False
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if sorted(s1) == sorted(s2):
        is_anagram = True

    return is_anagram


def dictionary_anagram_check(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False
    else:
        anagram_dict = {}
        for letter in s1:
            if letter in anagram_dict.keys():
                anagram_dict[letter] += 1
            else:
                anagram_dict[letter] = 1

        for letter in s2:
            if letter in anagram_dict.keys():
                anagram_dict[letter] -= 1
            else:
                return False

        for key in anagram_dict.keys():
            if anagram_dict[key] != 0:
                return False
        # print(anagram_dict)
        return True
# print(dictionary_method('Onder Eren', 'Soner Eren'))


def anagram_check(first_string, second_string):
    first_created_array = create_list(first_string.lower())
    second_created_array = create_list(second_string.lower())
    is_anagram = False

    if first_created_array.__eq__(second_created_array):
        is_anagram = True
    return is_anagram


def create_list(string_to_check):
    # print(f'Creating List for your text')
    created_array = []
    for letter in string_to_check:
        count = 1
        if letter != ' ':
            for elem in created_array:
                if letter == elem[0]:
                    element_to_remove = letter + elem[1]
                    # print(f'removing {element_to_remove}')
                    created_array.remove(element_to_remove)
                    count = int(elem[1]) + 1
                    break

            # print(f'count is {count}')
            letter_and_count = letter + str(count)
            created_array.append(letter_and_count)
            # print(f'adding {letter_and_count}')

    created_array.sort()

    # print(f'The array is {created_array}')
    return created_array


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        self.assertTrue(anagram_check('war', 'raw'))
        self.assertFalse(anagram_check('aa', 'bb'))
        self.assertTrue(anagram_check('clint eastwood', 'old west action'))
        self.assertTrue(anagram_check('go go go go', 'gggoooog'))
        self.assertTrue(anagram_check('abc', 'cba'))
        self.assertTrue(anagram_check('hi man', 'hi     man'))
        self.assertFalse(anagram_check('aabbcc', 'aabbc'))
        self.assertFalse(anagram_check('123', '1 2'))
        self.assertTrue(anagram_check('Onder', 'doner'))

    def test_easier_method(self):
        self.assertTrue(easier_anagram_check('war', 'raw'))
        self.assertFalse(easier_anagram_check('aa', 'bb'))
        self.assertTrue(easier_anagram_check('clint eastwood', 'old west action'))
        self.assertTrue(easier_anagram_check('go go go go', 'gggoooog'))
        self.assertTrue(easier_anagram_check('abc', 'cba'))
        self.assertTrue(easier_anagram_check('hi man', 'hi     man'))
        self.assertFalse(easier_anagram_check('aabbcc', 'aabbc'))
        self.assertFalse(easier_anagram_check('123', '1 2'))
        self.assertTrue(easier_anagram_check('Onder', 'doner'))

    def test_dictionary_method(self):
        self.assertTrue(dictionary_anagram_check('war', 'raw'))
        self.assertFalse(dictionary_anagram_check('aa', 'bb'))
        self.assertTrue(dictionary_anagram_check('clint eastwood', 'old west action'))
        self.assertTrue(dictionary_anagram_check('go go go go', 'gggoooog'))
        self.assertTrue(dictionary_anagram_check('abc', 'cba'))
        self.assertTrue(dictionary_anagram_check('hi man', 'hi     man'))
        self.assertFalse(dictionary_anagram_check('aabbcc', 'aabbc'))
        self.assertFalse(dictionary_anagram_check('123', '1 2'))
        self.assertTrue(dictionary_anagram_check('Onder', 'doner'))


if __name__ == '__main__':
    unittest.main()
