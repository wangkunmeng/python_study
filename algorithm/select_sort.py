def find_smallest(arr):
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[smallest_index]:
            continue
        smallest_index = i
    return smallest_index


print(find_smallest([1, 5, -1]))


def selector_sort(arr):
    sort = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        sort.append(arr.pop(smallest_index))
    return sort


print(selector_sort([4, 6, 5, 3, 1, 7]))
