

def check_even(x):
    even_num = False
    if x % 2 == 0:
        even_num = True
    return even_num


def square_func(x):
    return x**2


mylist = [x for x in range(15)]
filt_obj = filter(check_even, mylist)
map_obj = map(square_func, mylist)

even_num_list = list(filt_obj)
squared_num_list = list(map_obj)

print(f"even_num_list: {even_num_list}")
print(f"squared_num_list: {squared_num_list}")

filt_obj_with_lambda = filter(lambda x: x % 2 == 0, mylist)

print("Even numbers in the list: ", end='')
for elem in filt_obj_with_lambda:
    print(elem, end=',')

map_obj_with_lambda = map(lambda x: x**2, mylist)

print("\nSquared numbers in the list: ", end='')
for elem in map_obj_with_lambda:
    print(elem, end=',')
print('\n')
