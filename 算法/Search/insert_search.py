# coding=utf-8
# 插值查找, 要求数组有序且元素排列均匀
# mid = low + (high - low) * (key - a[low]) / (a[high] - a[low])


def insert_search(array, left, right, value):
    # print '1111'
    if value < array[0] or value > array[-1]:
        return -1
    mid_index = left + (right - left) * (value - array[left]) / (array[right] - array[left])
    mid_value = array[mid_index]
    if mid_value < value:
        return insert_search(array, mid_index + 1, right, value)
    elif mid_value > value:
        return insert_search(array, left, mid_index - 1, value)
    else:
        return mid_index


if __name__ == '__main__':
    arr = [-1000, -2, 0, 1, 3, 23, 45, 999, 100000]
    print insert_search(arr, 0, len(arr) - 1, 23)
