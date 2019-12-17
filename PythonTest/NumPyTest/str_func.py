# coding=utf-8
# 字符串函数
# 用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作

import numpy as np


if __name__ == '__main__':
    # 连接两个字符串
    print np.char.add(['hello '], ['world'])
    # 多重连接
    print np.char.multiply(['hello '], 3)
    # 将字符串居中, 并使用指定字符填充左右
    print np.char.center('hello', 20, fillchar='-')
    # 将字符串的第一个字母转大写
    print np.char.capitalize('hello hello hello')
    # 将字符串每一个单词首字母大写
    print np.char.title('hello hello hello')
    # 将数组元素转为小写
    print np.char.lower(['HELLO', 'WORLD'])
    # 将数组元素转大写
    print np.char.upper(['hello', 'world'])
    # 按指定分隔符分割字符串, 默认为' '
    print np.char.split('hello world')
    print np.char.split('hello\n world', '\n')
    print np.char.split('www.baidu.com', '.')
    # 以换行符作为分隔符来分割字符串
    print np.char.splitlines('hello\n world')
    # 移除开头或结尾处的特定字符
    print np.char.strip('ahello aworlda', 'a')  # 移除字符串头尾
    print np.char.strip(['ahello', 'aworlda', 'java'], 'a')  # 移除数组元素头尾
    # 通过指定分隔符连接数组中的元素或字符串
    print np.char.join('-', 'hello')
    print np.char.join(['-', ':'], ['hello', 'world'])
    # 使用新字符串替换字符串中所有指定的字串
    print np.char.replace('hello world', 'o', '0')
    # 对数组中的每个元素调用str.encode()
    print np.char.encode(['hello', 'world'], 'cp500')
    # 对数组中的每个元素调用str.decode()
    print np.char.decode(['\x88\x85\x93\x93\x96' '\xa6\x96\x99\x93\x84'], 'cp500')
