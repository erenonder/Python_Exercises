import ctypes
import sys

class DynamicArray():

    def __init__(self):

        self.capacity = 1
        self.number_of_elements = 0
        self.dynamic_array = self._create_array(self.capacity)

    def __len__(self):
        return self.number_of_elements

    def __repr__(self):
        string_to_show = f"[]"
        if self.number_of_elements == 0:
            string_to_show = "[]"
        else:
            string_to_show = "["
            for i in range(self.number_of_elements):
                if i == self.number_of_elements - 1:
                    string_to_show += f"{self.dynamic_array[i]}"
                else:
                    string_to_show += f"{self.dynamic_array[i]},"
            string_to_show += "]"

        return string_to_show

    def _create_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __getitem__(self, index):
        # print(f"index is {index} but number_of_elements is {self.number_of_elements}")
        if index < 0 or index >= self.number_of_elements:
            return IndexError(f'Out of bounds: there are {self.number_of_elements} item in the list, max index can be {self.number_of_elements - 1}')
        return self.dynamic_array[index]

    def append(self, element_to_append):
        if self.number_of_elements == self.capacity:
            self._resize_array(self.capacity * 2)

        self.dynamic_array[self.number_of_elements] = element_to_append
        self.number_of_elements += 1

    def _resize_array(self, new_capacity):
        # print(f"old size was: {sys.getsizeof(self.dynamic_array)}")
        new_array = self._create_array(new_capacity)

        # old_size = sys.getsizeof(new_array)

        for i in range(self.number_of_elements):
            # print(f"new len: {len(new_array)} old len: {len(self.dynamic_array)}")
            new_array[i] = self.dynamic_array[i]

        self.dynamic_array = new_array
        # print(f"new size is: {sys.getsizeof(self.dynamic_array)}")
        self.capacity = new_capacity


myarr = DynamicArray()

for i in range(10):
    myarr.append(i)
# myarr.append(4)
print(myarr)

