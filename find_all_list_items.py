

def index_all(search_list, item):
    index_list = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            index_list.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                # print(f'i {i} index {index} concat {[i] + index}')
                index_list.append([i] + index)
    return index_list


# example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3], 2]

# indice_list = index_all(example, 2)
# print(indice_list)
