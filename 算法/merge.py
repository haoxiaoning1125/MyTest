# coding=utf-8
# 合并两个有序数组


def merge_1(list1, list2):
    ret = []
    while list1 and list2:
        if list1[0] < list2[0]:
            ret.append(list1.pop(0))
        else:
            ret.append(list2.pop(0))
    return ret + list1 + list2


def merge_2(list1, list2):
    m = len(list1)
    n = len(list2)
    list1 += [None for _ in range(n)]
    while m > 0 and n > 0:
        if list2[n - 1] > list1[m - 1]:
            list1[m + n - 1] = list2[n - 1]
            n -= 1
        else:
            list1[m + n - 1] = list1[m - 1]
            m -= 1
    if n > 0:
        list1[:n] = list2[:n]
    return list1.remove(None)


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    a = a[0:3]
    print merge_1(a, b)
