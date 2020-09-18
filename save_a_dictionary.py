import os
import re
from pydoc import locate
import unittest
import pickle

cwd = os.getcwd()
# print(f'cwd: {cwd}')


def save_dictionary(dict_to_save, path_to_file):
    # print(f'file will be saved to {path_to_file} and dict is {dict_to_save}')
    with open(f'{path_to_file}/onder.txt', 'w') as dict_store_file:
        for key in dict_to_save.keys():
            dict_store_file.write(f'{key} {type(key)}: {dict_to_save[key]} {type(dict_to_save[key])}\n')


def save_dictionary_with_pickle(dict_to_save, path_to_file):
    with open(f'{path_to_file}/onder.txt', 'wb') as dict_store_file:
        pickle.dump(dict_to_save, dict_store_file)


def load_dictionary_with_pickle(path_to_file):
    with open(path_to_file, 'rb') as dict_load_file:
        return pickle.load(dict_load_file)


def load_dictionary(path_to_file):
    loaded_dict = dict()
    with open(path_to_file, 'r') as dict_to_load:
        file_content = dict_to_load.readlines()

    for line in file_content:
        # print(f'LINE: {line}')
        # splitted = line.split(':')
        # print(splitted[0])
        match = re.findall(r"(\w+) <class '(\w+)'>: (\w+) <class '(\w+)'>", line)
        # print(match)

        if len(match) != 0:
            dict_key = match[0][0]
            key_type = locate(match[0][1])
            dict_val = match[0][2]
            val_type = locate(match[0][3])
            # print(f'key_type: {key_type} key: {dict_key} val_type: {val_type} val: {dict_val}')
            loaded_dict[key_type(dict_key)] = val_type(dict_val)
        else:
            print('No match found')

    return loaded_dict


class TestDict(unittest.TestCase):

    def test_save_load_dict_1(self):

        save_dict = {'onder': 7, 'nihan': 3}
        save_dictionary(save_dict, cwd)

        return_dict = load_dictionary(f'{cwd}/onder.txt')

        self.assertEqual(return_dict, save_dict)

    def test_save_load_dict_2(self):

        save_dict = {'onder': 'eren', 'nihan': 'ocak'}
        save_dictionary(save_dict, cwd)

        return_dict = load_dictionary(f'{cwd}/onder.txt')

        self.assertEqual(return_dict, save_dict)

    def test_save_load_dict_3(self):

        save_dict = {'onder': [1, 2, 3], 'nihan': [4, 5, 6]}
        save_dictionary_with_pickle(save_dict, cwd)

        return_dict = load_dictionary_with_pickle(f'{cwd}/onder.txt')

        self.assertEqual(return_dict, save_dict)

    def test_save_load_dict_4(self):

        save_dict = {'onder': [[1, 2, 3], 'onder'], 'nihan': ([4, 5, 6], 'nihan', 'a', 3)}
        save_dictionary_with_pickle(save_dict, cwd)

        return_dict = load_dictionary_with_pickle(f'{cwd}/onder.txt')

        self.assertEqual(return_dict, save_dict)


if __name__ == '__main__':
    unittest.main()
