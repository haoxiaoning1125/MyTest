# coding=utf-8
# n维数组对象 ndarray

import numpy as np


if __name__ == '__main__':
    a = np.array([1, 2, 3])
    print a

    b = np.array([[1, 2], [3, 4]])
    print b

    c = np.array([1, 2, 3], ndmin=2)
    print c

    d = np.array([1, 2, 3], dtype=complex)
    print d
