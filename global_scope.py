
num = 42

def change_num():
    global num
    num = 43
    print(f'num in func {num}')

change_num()
print(f'num in globe {num}')