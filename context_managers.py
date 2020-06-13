# context managers
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()

with open_file("sample.txt", "w") as file:
    file.write("context manager with function")

# with open("sample.txt", "w") as myfile:
#     myfile.write("Onder Eren")

# class MyContextManager:

#     def __init__(self, filename, mode):
#         print('Init method')
#         self.filename = filename
#         self.file = None
#         self.mode = mode

#     def __enter__(self):
#         print("Enter method")
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         print("Exit method")
#         self.file.close()


# with MyContextManager("sample.txt", "w") as mcm:
#     mcm.write("Testing")

# print(mcm.closed)
