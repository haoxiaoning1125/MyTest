# coding=utf-8
# 算数函数

import numpy as np


if __name__ == '__main__':
    # np.reciprocal(): 倒数
    a = np.array([0.25, 1.33, 1, 100])
    print a
    print np.reciprocal(a)
    print '-' * 20

    # np.power(a, b): a ** b
    a = np.array([-1, 0, 1, 2, 3])
    print np.power(a, 2)
    print np.power(np.array([2, 3, 4]), np.array([1, 2, 3]))
    print '-' * 20

    # np.mod(), np.remainder(): 求余
    a = np.array([10, 20, 30])
    b = np.array([3, 7, 11])
    print np.mod(a, b)
    print np.remainder(a, b)
