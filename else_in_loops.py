# else in loops

def find_index(to_search, target):
    i = 0
    for i, value in enumerate(to_search):
        if(value == target):
            break
    else:
        return -1
    return i


mylist = ["Onder", "Soner", "Nihan"]
print(find_index(mylist, "Nihan"))
