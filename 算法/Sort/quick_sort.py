# coding=utf-8

import random


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [num for num in array[1:] if num < pivot]
    more = [num for num in array[1:] if num > pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)


if __name__ == '__main__':
    array = [random.randint(1, 100) for i in range(20)]
    print array
    array = quick_sort(array)
    print array
