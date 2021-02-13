import os
import argparse

def main():

    parser = argparse.ArgumentParser(
        description='Removes the spaces in a given folder name')
    parser.add_argument('-n', '--name', type=str, default='/Users/ondereren/Downloads',
                        help='Destination of the directory to look for spaces')

    args = parser.parse_args()

    fix_spaces(args.name)


def update_file_name(directory_checked, file_name):
    if file_name[0] == '.':
        pass
    else:
        if file_name[0] == '-':
            # just do operation on this when tested
            pass
        else:
            new_file_name = file_name
            if " " in file_name:
                # print(
                    # f"This folder name includes spaces: {file_name} without spaces will be {file_name.replace(' ','_')}")
                new_file_name = file_name.replace(' ', '_')
                # print(f'{file_name} --> {new_folder_name}')
                os.rename(f'{directory_checked}/{file_name}',
                          f'{directory_checked}/{new_file_name}')
                return new_file_name
            else:
                if os.path.isdir(os.path.join(directory_checked, file_name)):
                    # Directory name not changed but there can be files to be checked inside
                    # so return the new_file_name anyways
                    return new_file_name
                else:
                    pass

def fix_spaces(directory_checked):

    list_dir = None

    try:
        list_dir = os.listdir(directory_checked)
    except PermissionError:
        pass
    except FileNotFoundError:
        print('No Such Destination')
    finally:
        pass
        # print('Directory Contents:')
        # print(list_dir)

    if list_dir:
        for elem in list_dir:
            # print(f"elem: {elem}")
            if os.path.isdir(os.path.join(directory_checked, elem)):
                # In directories there needs to be a recursive loop to check inner files and folders
                new_name = update_file_name(directory_checked, elem)
                # print(f'File name was: {elem} and now: {new_name}')
                if new_name:
                    # print(f'File name was: {elem} and now: {new_name}')
                    # print(
                        # f'Directory checked was: {directory_checked} and now: {directory_checked}/{new_name}')
                    fix_spaces(f"{directory_checked}/{new_name}")

            elif os.path.isfile(os.path.join(directory_checked, elem)):
                update_file_name(directory_checked, elem)
            else:
                pass


if __name__ == "__main__":
    main()
