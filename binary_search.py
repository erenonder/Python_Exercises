

def rec_bin_search(arr, ele):
    found = False

    if len(arr) == 1 and ele == arr[0]:
        return True
    elif len(arr) == 1 and ele != arr[0]:
        return False
    else:
        mid = int(len(arr) / 2)
        if arr[mid] == ele:
            found = True
            # print(f'returning found: {found} and mid: {mid}')
            return found
        if arr[mid] > ele:
            return rec_bin_search(arr[:mid], ele)
        elif arr[mid] < ele:
            return rec_bin_search(arr[mid:], ele)


if __name__ == '__main__':
    arr = []
    ele = 50
    for i in range(500):
        arr.append(i)

    found = rec_bin_search(arr, ele)
    print(f'{ele} is {"FOUND" if found else "NOT FOUND"}')
