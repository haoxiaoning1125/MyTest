# coding=utf-8
# 数组属性

import numpy as np


if __name__ == '__main__':
    # ndim: 秩
    a = np.arange(24)
    print a.ndim
    a = a.reshape(2, 4, 3)
    print a.ndim
    print '-' * 20

    # shape: 维度
    a = np.array([
        [1, 2, 3],
        [1, 2, 3]
    ])
    print a.shape  # (2, 3), 2行3列
    a.shape = (3, 2)
    print a
    a = a.reshape(2, 3)
    print a
    print '-' * 20

    # itemsize: 每个元素的大小, n个字节
    x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    print x.itemsize
    y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    print y.itemsize
    print '-' * 20

    # flags: 内存信息
    print x.flags
    print '-' * 20

    '''
        ndarray.*
        ndim: 秩
        shape: 维度
        size: 元素个数
        dtype: 元素类型
        itemsize: 每个元素的大小, 以字节为单位
        flags: numpy对象的内存信息
        real: 元素实部
        imag: 元素虚部
        data: 包含实际数组元素的缓冲区
    '''