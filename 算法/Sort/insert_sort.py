# coding=utf-8

import random


def insert_sort(array):
    for i in range(len(array)):
        pre_index = i - 1
        current = array[i]
        while pre_index >= 0 and array[pre_index] > current:
            array[pre_index + 1] = array[pre_index]
            pre_index -= 1
        array[pre_index + 1] = current
    return array


if __name__ == '__main__':
    array = [random.randint(1, 100) for i in range(20)]
    print array
    array = insert_sort(array)
    print array
