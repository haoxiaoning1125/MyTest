# coding=utf-8
# 副本和视图

import numpy as np


if __name__ == '__main__':
    # 视图, 浅拷贝
    a = np.arange(6).reshape(3, 2)
    print a
    b = a.view()
    print b
    print (id(a), id(b))
    b.shape = 2, 3
    print a
    print b
    print '-' * 20

    # 使用切片创建视图会修改原始数组
    a = np.arange(12)
    print a
    x = a[3:]
    y = a[3:]
    x[1] = 123
    y[2] = 456
    print a
    print id(x), id(y), id(a[3:])
    print '-' * 20

    # 副本, 深拷贝
    a = np.array([
        [10, 10], [2, 3], [4, 5]
    ])
    print a
    b = a.copy()
    print b
    print b is a
    b[0, 0] = 100
    print a
    print b
