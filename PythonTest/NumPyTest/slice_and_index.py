# coding=utf-8
# 切片和索引

import numpy as np


if __name__ == '__main__':
    # 一维数组
    a = np.arange(10)
    print a
    print a[slice(2, 7, 2)]
    print a[2: 7: 2]
    print '-' * 20

    # 多维数组
    b = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print b
    print b[1:]
    print b[..., 1]  # 第2列
    print b[1, ...]  # 第2行
    print b[..., 1:]  # 第2列以及剩下的所有元素
