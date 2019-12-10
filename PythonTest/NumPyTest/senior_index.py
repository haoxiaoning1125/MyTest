# coding=utf-8
# 高级索引

import numpy as np


if __name__ == '__main__':
    # 整数数组索引
    x = np.array([
        [1, 2], [3, 4], [5, 6]
    ])
    print x[[0, 1, 2], [0, 1, 0]]  # [0][0], [1][1], [2][0]

    # 布尔索引
    x = np.array([
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]
    ])
    print x[x > 5]  # 大于5的元素

    # 布尔索引过滤 NaN
    x = np.array([
        [np.nan, 1, 2, 3, np.nan, 4, 5]
    ])
    print x[~np.isnan(x)]

    # 布尔值索引过滤非复数
    x = np.array([
        1, 2 + 6j, 5, 3.5 + 5j
    ])
    print x[np.iscomplex(x)]
