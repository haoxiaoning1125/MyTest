# coding=utf-8

import random


def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    array = [random.randint(1, 100) for i in range(20)]
    print array
    array = bubble_sort(array)
    print array
