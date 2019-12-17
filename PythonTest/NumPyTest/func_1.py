# coding=utf-8
# 数学函数

import numpy as np


if __name__ == '__main__':
    # 三角函数
    a = np.array([0, 30, 45, 60, 90])
    print np.sin(a * np.pi / 180)
    print np.cos(a * np.pi / 180)
    print np.tan(a * np.pi / 180)
    print '-' * 20

    # 舍入函数
    a = np.array([1.0, 5.55, 123, 0.567, 25.532])
    print a
    print np.around(a)
    print np.around(a, decimals=1)
    print np.around(a, decimals=-1)  # decimals: 舍入的小数位数, 默认值为0, 如果为负, 整数将四舍五入到小数点左侧的位置
    print '-' * 20

    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print a
    print np.floor(a)  # 返回小于等于指定表达式的最大整数, 向下取整
    print '-' * 20

    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print a
    print np.ceil(a)  # 返回大于等于指定表达式的最小整数, 向上取整
