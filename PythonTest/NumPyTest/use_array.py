# coding=utf-8
# 数组操作

import numpy as np


if __name__ == '__main__':
    # numpy.ndarray.reshape(): 修改数组形状
    # order: 'C': 按行, 'F': 按列, 'A': 原顺序
    a = np.arange(8)
    print a
    print a.reshape(2, 4, order='C')
    print '-' * 20

    # numpy.ndarray.flat: 数组元素迭代
    a = np.arange(9).reshape(3, 3)
    print [num for num in a.flat]
    print '-' * 20

    # numpy.ndarray.flatten(): 返回一份数组拷贝
    print a.flatten()
    print '-' * 20

    # numpy.ravel(): 展平数组元素, 返回数组视图, 修改会影响原始数组
    print a.ravel()
    print '-' * 20

    # numpy.transpose(): 对换数组的维度
    a = np.arange(8).reshape(2, 4)
    print a
    print a.transpose()
    print '-' * 20

    # numpy.split(): 分割数组
    a = np.arange(9)
    print a
    print np.split(a, 3)  # 分割为3个大小相等的子数组
    print np.split(a, [4, 7])  # 按给定的下表分割
    print '-' * 20

    # numpy.hsplit(): 水平分割数组, 把行切断
    a = np.floor(10 * np.random.random((2, 6)))
    print a
    print np.hsplit(a, 3)  # 返回3个形状相同的数组
    print '-' * 20

    # numpy.vsplit(): 垂直分割数组, 把列切断
    a = np.arange(16).reshape(4, 4)
    print a
    print np.vsplit(a, 2)
    print '-' * 20

    # numpy.resize(): 返回指定大小的新数组, 如果新数组大于原数组, 则包含原数组中元素的副本
    a = np.array([
        [1, 2, 3], [4, 5, 6]
    ])
    print a
    print a.shape
    b = np.resize(a, (3, 2))
    print b
    print b.shape
    b = np.resize(a, (3, 3))
    print b
    print b.shape
    print '-' * 20

    # numpy.append(): 在数组末尾添加值
    a = np.array([
        [1, 2, 3], [4, 5, 6]
    ])
    print a
    print np.append(a, [7, 8, 9])
    print np.append(a, [[7, 8, 9]], axis=0)  # 沿轴0添加
    print np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1)  # 沿轴1添加
    print '-' * 20

    # numpy.insert(): 沿给定轴往数组中插入值
    a = np.array([
        [1, 2], [3, 4], [5, 6]
    ])
    print a
    print np.insert(a, 3, [11, 12])  # 未传递axis, 在插入前数组被展开
    print np.insert(a, 1, 11, axis=0)  # axis=0, 插入一行并广播
    print np.insert(a, 1, 11, axis=1)  # axis=1, 插入一列并广播
    print '-' * 20

    # numpy.delete(): 返回从输入数组中删除指定子数组的新数组
    a = np.arange(12).reshape(3, 4)
    print a
    print np.delete(a, 5)  # 未传递axis, 展开数组并删除第5个元素
    print np.delete(a, 0, axis=0)  # 删除第0行
    print np.delete(a, 0, axis=1)  # 删除第0列
    print '-' * 20

    # numpy.unique(): 去除数组中的重复元素
    a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
    print a
    print np.unique(a)
    print np.unique(a, return_index=True)  # 返回去重数组的索引数组
