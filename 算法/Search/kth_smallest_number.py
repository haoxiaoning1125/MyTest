# coding=utf-8
# 寻找序列中第k小的元素

import random


def find_kth_smallest_1(data, k):
    if not 0 <= k < len(data):
        raise ValueError('k is out of range.')
    while True:
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
        if k < len(low):
            data = low
        elif k < len(low) + pcount:
            return pivot
        else:
            data = high
            k -= len(low) + pcount


def find_kth_smallest_2(data, k):
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
    if k < len(low):
        return find_kth_smallest_2(low, k)
    elif k < len(low) + pcount:
        return pivot
    else:
        return find_kth_smallest_2(high, k - len(low) - pcount)


if __name__ == '__main__':
    arr = range(20)
    # print find_kth_smallest_1(arr, 0)
    print find_kth_smallest_2(arr, 0)
