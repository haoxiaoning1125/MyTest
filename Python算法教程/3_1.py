# coding=utf-8

import random


def gnome_sort(seq):
    # 侏儒排序法
    i = 0
    while i < len(seq):
        if i == 0 or seq[i - 1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1


def merge_sort(seq):
    mid = len(seq) / 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res


if __name__ == '__main__':
    seq = [random.randint(0, 100) for _ in range(20)]
    print seq
    gnome_sort(seq)
    print seq
    print '-' * 20

    seq = [random.randint(0, 100) for _ in range(20)]
    print seq
    seq = merge_sort(seq)
    print seq
