# coding=utf-8
# 有序字典

from collections import OrderedDict

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print d
    # od 的 key 按照插入顺序排列
    od = OrderedDict(d)
    print od
