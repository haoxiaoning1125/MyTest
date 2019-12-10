# coding=utf-8

import numpy as np


if __name__ == '__main__':
    # 创建数组
    # numpy.empty
    x = np.empty([3, 2], dtype=int)
    print x
    print '-' * 20

    # numpy.zeros
    x = np.zeros(5, dtype=np.int)
    print x
    x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'f4')])
    print x
    print '-' * 20

    # numpy.ones
    x = np.ones(5, dtype=np.int)
    print x
    x = np.ones([2, 2], dtype=np.int)
    print x
    print '-' * 20

    # 从已有的数组创建数组
    # numpy.asarray
    x = [1, 2, 3]
    a = np.asarray(x)
    print a
    x = [(1, 2, 3), (4, 5)]
    a = np.asarray(x)
    print a
    x = [1, 2, 3]
    a = np.asarray(x, dtype=np.float32)
    print a
    print '-' * 20

    # numpy.frombuffer
    s = 'Hello World'
    a = np.frombuffer(s, dtype='S1')
    print a
    print '-' * 20

    # numpy.fromiter
    li = range(10)
    it = iter(li)
    a = np.fromiter(it, dtype=np.int)
    print a
    it = iter(li)
    a = np.fromiter(it, dtype=np.int, count=5)  # count: 读取多少数据, 默认为-1, 全部读取
    print a
    print '-' * 20

    # 从数值范围创建数组
    # numpy.arange
    a = np.arange(start=0, stop=10, step=2, dtype=np.int)
    print a
    a = np.arange(0, 10, 2, np.float64)
    print a
    print '-' * 20
    # numpy.linspace, 创建等差数列一维数组
    a = np.linspace(1, 10, 5)
    print a
    print '-' * 20
    # numpy.logspace, 创建等比数列一维数组
