#!/usr/local/bin/python3.8

import os


class Colors:
    PINK = '\033[95m'
    DARKBLUE = '\033[94m'
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

class Tree:

    def __init__(self):

        self.file_count = 0
        self.dir_count = 0

    def print_directory_content(self, directory_checked='.'):

        list_dir = None

        if(directory_checked == '.'):
            current_dir = os.getcwd()
            print(current_dir)
            indent_count = 0
        else:
            relative_path = os.path.relpath(directory_checked, '.')
            indent_count = len(relative_path.split('/'))

        try:
            list_dir = os.listdir(directory_checked)
        except PermissionError:
            pass

        if list_dir:
            for elem in list_dir:

                if os.path.isdir(os.path.join(directory_checked, elem)):

                    self.dir_count += 1
                    self.indentation_check(directory_checked, indent_count)

                    print('|', end='')
                    print(f"__{Colors.YELLOW}{elem}{Colors.END}")
                    new_directory_name = os.path.join(directory_checked, elem)
                    self.print_directory_content(new_directory_name)

                elif os.path.isfile(os.path.join(directory_checked, elem)):

                    self.file_count += 1
                    self.indentation_check(directory_checked, indent_count)

                    print('|', end='')
                    print(f"__{Colors.GREEN}{elem}{Colors.END}")

    def indentation_check(self, directory_checked, indent_count):
        if directory_checked != '.':
            print(' ' * (indent_count * 3), end='')
        else:
            pass

    def print_file_counts(self):
        print(f'{self.dir_count} directories, {self.file_count} files')


# $ tree path/to/folder/
# path/to/folder/
# ├── a-first.html
# ├── b-second.html
# ├── subfolder
# │   ├── readme.html
# │   ├── code.cpp
# │   └── code.h
# └── z-last-file.html

# 1 directories, 6 files

if __name__ == '__main__':
    tree = Tree()
    tree.print_directory_content()
    tree.print_file_counts()
