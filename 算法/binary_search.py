# coding=utf-8
# 二分查找


def binary_search(arr, value):
    result = -1
    low = 0
    high = len(arr)

    while low <= high:
        middle = int((high - low) / 2) + low

        if arr[middle] == value:
            return middle
        elif arr[middle] < value:
            low = middle + 1
        else:
            high = middle - 1

    return result


if __name__ == '__main__':
    arr1 = [1, 3, 16, 23, 25, 32, 79]
    arr2 = [1, 3, 16, 23, 25, 32]

    for i in arr1:
        print 'index: {}, num: {}'.format(binary_search(arr1, i), i)
    print '-' * 20

    for i in arr2:
        print 'index: {}, num: {}'.format(binary_search(arr2, i), i)
