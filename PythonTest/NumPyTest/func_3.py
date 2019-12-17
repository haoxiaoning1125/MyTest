# coding=utf-8
# 统计函数

import numpy as np


if __name__ == '__main__':
    # np.amin(): 计算数组沿指定轴的最小值
    # np.amax(): 计算数组沿指定轴的最大值
    a = np.array([
        [3, 7, 5], [8, 4, 3], [2, 4, 9]
    ])
    # print a
    print np.amin(a, 0)  # 纵
    print np.amin(a, 1)  # 横
    print np.amax(a)
    print np.amax(a, axis=0)
    print np.amax(a, axis=1)
    print '-' * 20

    # np.ptp(): 计算数组中最大与最小元素的差
    a = np.array([
        [3, 7, 5], [8, 4, 3], [2, 4, 9]
    ])
    print np.ptp(a)
    print np.ptp(a, 0)
    print np.ptp(a, 1)
    print '-' * 20

    # np.percentile(): 百分位数, 小于这个值的观察值的百分比
    a = np.array([
        [10, 7, 4], [3, 2, 1]
    ])
    print np.percentile(a, 50)
    print '-' * 20  # ???


