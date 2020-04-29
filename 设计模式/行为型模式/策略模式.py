# coding=utf-8
# 例: 实现算法, 检测在一个字符串中是否所有的字符都是唯一的

import time


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


SLOW = 3
LIMIT = 5
WARNING = 'too bad, you picked the slow algorithm.'


# 检测长字符串能力较差
def all_unique_sort(s):
    if len(s) > LIMIT:
        print WARNING
        time.sleep(SLOW)
    if len(s) == 1:
        return True
    srt_str = sorted(s)
    for c1, c2 in pairs(srt_str):
        if c1 == c2:
            return False
    return True


# 检测短字符串能力较差
def all_unique_set(s):
    if len(s) < LIMIT:
        print WARNING
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


# 保留两个算法, 根据输入字符串的长度选择调用
def all_unique(s, strategy):
    return strategy(s)


if __name__ == '__main__':
    while True:
        word = None
        while not word:
            word = raw_input('input a word(quit to exit): ')
        if word == 'quit':
            break
        else:
            strategy_list = [all_unique_sort, all_unique_set]
            strategy_picked = strategy_list[len(word) > LIMIT]
            print all_unique(word, strategy_picked)
