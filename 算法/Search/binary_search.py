# coding=utf-8
# 二分查找, 有序序列
# mid = (low + high) / 2 = low + (high - low) / 2


def binary_search(arr, value):
    result = -1
    low = 0
    high = len(arr)
    while low <= high:
        # print '1111'
        middle = low + ((high - low) >> 1)  # 位运算符优先级低于算术运算符
        if arr[middle] == value:
            return middle
        elif arr[middle] < value:
            low = middle + 1
        else:
            high = middle - 1
    return result


if __name__ == '__main__':
    arr = [-1000, -2, 0, 1, 3, 23, 45, 999, 100000]
    print binary_search(arr, 23)
