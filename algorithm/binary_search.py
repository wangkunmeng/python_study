def binary_search(list, item):
    """二分查找算法"""
    low = 0
    high = len(list) - 1
    if high > 10000:
        if item > list[high]:
            return -1
        if item < list[low]:
            return -1
        if item == list[low]:
            return low
        if item == list[high]:
            return high
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search([1, 3, 5, 7, 9], 7))
print(binary_search([1, 3, 5, 7, 9], 8))
print(7 / 2, 7 // 2, 17 // 4)
