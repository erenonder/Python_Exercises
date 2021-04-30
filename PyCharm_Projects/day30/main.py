
# file_content = ""
#
# try:
#     with open("onder.txt") as file:
#         file_content = file.read()
# except FileNotFoundError as error_message:
#     print(f"There is an exception {error_message}")
#
# print(file_content)
#
# a_dict = {"Onder": 1, "Nihan": 2}
#
# try:
#     print(a_dict["Onderx"])
# except KeyError as error_message:
#     print(f"Key {error_message} does not exist")
# else:
#     print("In else")
# finally:
#     print("In finally")
#
#
# class Onder(Exception):
#     pass
#
# try:
#     raise Onder("My own exception")
# except Onder as error_message:
#     print(f"Exception Occ: {error_message}")