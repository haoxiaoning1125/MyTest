# coding=utf-8

import random


def merge(list1, list2):
    ret = []
    while list1 and list2:
        if list1[0] < list2[0]:
            ret.append(list1.pop(0))
        else:
            ret.append(list2.pop(0))
    return ret + list1 + list2


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) / 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


if __name__ == '__main__':
    array = [random.randint(1, 100) for i in xrange(20)]
    print array
    array = merge_sort(array)
    print array
