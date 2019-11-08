# coding=utf-8
# 计数器

from collections import Counter

if __name__ == '__main__':
    c = Counter()
    for i in 'programmer':
        c[i] += 1
    print c
