# coding=utf-8
# 排序, 条件刷选函数

import numpy as np


if __name__ == '__main__':
    # np.sort(): 返回输入数组的排序副本
    a = np.array([
        [3, 7, 5], [6, 9, 1], [2, 5, 1]
    ])
    print np.sort(a)  # 默认按行排序
    print np.sort(a, axis=0)  # 按列排序
    print np.sort(a, axis=1)  # 按行排序
    print '-' * 20

    # np.argsort(): 返回数组值从小到大的索引
    a = np.array([3, 2, 1])
    y = np.argsort(a)
    print y
    print a[y]
    print '-' * 20

    # np.lexsort(): 对多个序列进行排序
    m = (10, 20, 50, 10)
    c = (30, 50, 40, 60)
    t = (40, 70, 90, 70)
    ind = np.lexsort((m, c, t))  # 优先级高的项在后
    for i in ind:
        print [m[i], c[i], t[i]]
    print '-' * 20

    # np.argmax(), np.argmin(): 分别沿给定轴返回最大和最小元素的索引
    a = np.array([
        [30, 40, 70], [80, 20, 10], [50, 90, 60]
    ])
    print np.argmax(a)  # 将数组展开
    print np.argmax(a, axis=0)  # 按列
    print np.argmax(a, axis=1)  # 按行
    print np.argmin(a)  # 将数组展开
    print np.argmin(a, axis=0)  # 按列
    print np.argmin(a, axis=1)  # 按行
    print '-' * 20

    # np.nonzero(): 返回输入数组中非零元素的索引
    a = np.array([
        [30, 40, 0], [0, 20, 10], [50, 0, 60]
    ])
    print np.nonzero(a)  # (array([0, 0, 1, 1, 2, 2]), array([0, 1, 1, 2, 0, 2])), ((xs), (ys))
    print '-' * 20

    # np.where(): 返回输入数组中满足给定条件的元素索引
    a = np.arange(9).reshape(3, 3)
    print a
    print np.where(a > 3)  # ((xs), (ys))
    print '-' * 20

    # np.extract(): 根据某个条件从数组中抽取元素, 返回满足条件的元素
    a = np.arange(9).reshape(3, 3)
    print a
    print np.extract(a > 3, a)
