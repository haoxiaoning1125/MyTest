# coding=utf-8
# 默认字典, key不存在时, 返回默认值

from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    l = [1, 2, 3, 4, 5]
    for i in l:
        d[str(i)].append(i)
    print d

    d['test'] = 10
    print d

    print d['none']
