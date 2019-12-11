# coding=utf-8
# 广播

import numpy as np


if __name__ == '__main__':
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    c = a * b
    print c
    print '-' * 20

    # 参与运算的数组形状不同时, numpy自动触发广播机制
    a = np.array([
        [0, 0, 0], [10, 10, 10], [20, 20, 20], [40, 40, 40]
    ])
    b = np.array([1, 2, 3])
    print 'a * b =\n{}'.format(a * b)
    print 'a + b =\n{}'.format(a + b)
    print '-' * 20

    # ValueError: operands could not be broadcast together with shapes (4,3) (2)
    # a = np.array([
    #     [0, 0, 0], [10, 10, 10], [20, 20, 20], [40, 40, 40]
    # ])
    # b = np.array([1, 2])
    # print 'a * b =\n{}'.format(a * b)
    # print 'a + b =\n{}'.format(a + b)

    '''
        让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
        输出数组的形状是输入数组形状的各个维度上的最大值。
        如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
        当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。
        
        若条件不满足，抛出 "ValueError: frames are not aligned" 异常
    '''
