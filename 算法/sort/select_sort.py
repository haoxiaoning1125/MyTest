# coding=utf-8

import random


def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    array = [random.randint(1, 100) for i in range(20)]
    print array
    array = selection_sort(array)
    print array
