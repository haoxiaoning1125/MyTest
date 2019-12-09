# coding=utf-8
# numpy 的数据类型

import numpy as np


if __name__ == '__main__':
    # 标量类型
    print np.dtype(np.int32)

    # int8, int16, int32, int64 可用 'i1', 'i2', 'i4', 'i8' 代替, 'in'代表n个字节
    print np.dtype('i4')

    # 字节顺序标注,
    # "<"意味着小端法(最小值存储在最小的地址，即低位组放在最前面)
    # ">"意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)
    print np.dtype('<i4')
    print '-' * 20

    # 结构化数据类型
    dt = np.dtype([('age', np.int8)])
    print dt

    # 结构化类型应用于数据对象
    a = np.array([(10,), (20,), (30,)], dtype=dt)
    print a

    # 类型字段名用来存取列
    print a['age']
    print '-' * 20

    # 多个属性的结构化数据类型
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    print student
    a = np.array([
        ('aaa', 21, 100),
        ('bbb', 22, 70),
        ('ccc', 23, 59)
    ], dtype=student)
    print a
    print a['name']
    print a['age']
    print a['marks']

    '''
    内建类型对应的字符代码:
    ---------------------------------
        b     |  布尔型
        i     |  有符号整型
        u     |  无符号整型
        f     |  浮点型
        c     |  复数浮点型
        m     |  timedelta(时间间隔)
        M     |  datetime(日期时间)
        O     |  python对象
        S, a  |  byte-字符串
        U     |  unicode
        V     |  void
    ---------------------------------
    '''
