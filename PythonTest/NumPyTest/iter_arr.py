# coding=utf-8
# 迭代数组

import numpy as np


if __name__ == '__main__':
    a = np.arange(6).reshape(2, 3)  # (2, 3) --> 2行3列
    print a
    print [x for x in np.nditer(a)]  # 默认按行遍历
    print [x for x in np.nditer(a.T)]
    print [x for x in np.nditer(a.T.copy(order='C'))]  # 按列遍历
    print '-' * 20

    # 控制遍历顺序
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print '原始数组:\n{}'.format(a)
    print '转置:\n{}'.format(a.T)
    print 'C风格:\n{}'.format(a.T.copy(order='C'))
    print 'F风格:\n{}'.format(a.T.copy(order='F'))
    print '-' * 20

    # 修改数组中元素
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print a
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = 2 * x
    print a
    print '-' * 20

    # 使用外部循环
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print a
    print [x for x in np.nditer(a, flags=['external_loop'], order='F')]
    print '-' * 20

    # 广播迭代
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print a
    b = np.array([
        1, 2, 3, 4
    ], dtype=int)
    print b
    for x, y in np.nditer([a, b]):
        print (x, y)
