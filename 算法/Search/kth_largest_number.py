# coding=utf-8
# 序列中第k大的元素

import random


def find_kth_largest(data, k):
    if not 0 <= k < len(data):
        raise ValueError('k is out of range.')
    pivot = random.choice(data)
    pcount = 0
    low, high = [], []
    for elem in data:
        if elem < pivot:
            low.append(elem)
        elif elem > pivot:
            high.append(elem)
        else:
            pcount += 1
    if k < len(high):
        return find_kth_largest(high, k)
    elif k < len(high) + pcount:
        return pivot
    else:
        return find_kth_largest(low, k - len(high) - pcount)


if __name__ == '__main__':
    arr = range(10)
    print find_kth_largest(arr, 0)
