# coding=utf-8
# math库函数

import math


if __name__ == '__main__':
    # 大于等于x的最小整数
    print math.ceil(4.12)
    print math.ceil(5)
    # 小于等于x的最大整数
    print math.floor(4.12)
    print math.floor(4)
    # 把y的符号加到x前
    print math.copysign(2, -1)
    print math.copysign(-1, -1)
    # sin...
    print math.sin(math.pi / 4)
    print math.cos(math.pi / 4)
    print math.tan(math.pi / 4)
    # e
    print math.e
    # e ** x
    print math.exp(2)
    # e ** x - 1
    print math.expm1(2)
    # 余数, float
    print math.fmod(20, 3)
    # 求和
    print math.fsum((1, 2, 3, 4))
    # 开方 x ** 2 + y ** 2
    print math.hypot(3, 4)
    # 是否为无穷大
    print math.isinf(1)
    # log4(2)
    print math.log(2, 4)
    # 开方
    print math.sqrt(10)
    # 返回整数部分
    print math.trunc(2.1)
