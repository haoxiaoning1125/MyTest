# coding=utf-8
# 四叶草主题

import pylab as pl
from time import sleep
import random
# from pprint import pprint


J = 0.1  # 罐子
X = 0.7  # 三叶草
Y = 0.1  # 四叶草
K = 5
N = 3
Z = 8
PRO_1 = [J, J + X, J + X + Y, 1.0]  # 正常
PRO_2 = [J, J + X + Y, J + X + Y, 1.0]  # 四叶草满
PRO_3 = [0, J + X, J + X + Y, 1.0]  # 罐子满
PRO_4 = [0, J + X + Y, J + X + Y, 1.0]  # 四叶草，罐子满


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    random.shuffle(arr)
    return arr


def random_mark_result(jug, clover):
    """
    :return: 0: 罐子, 1: 三叶草, 2: 四叶草, 3: 空
    """
    if jug < K:
        if clover < N:
            pro = PRO_1
        else:
            pro = PRO_2
    else:
        if clover < N:
            pro = PRO_3
        else:
            pro = PRO_4
    r = random.random()
    for index, num in enumerate(pro):
        if r < num:
            return index
    return 3


def check_jug_around(bingo_map, x, y):
    for x_ in range(max(0, x - 1), min(4, x + 1) + 1):
        for y_ in range(max(0, y - 1), min(4, y + 1) + 1):
            if bingo_map[x_][y_] >= 0:
                return True
    return False


def one_mark(bingo_map, x, y, mark_count):
    jug, clover = mark_count
    if jug < K and not check_jug_around(bingo_map, x, y):
        mark_result = 0
    else:
        mark_result = random_mark_result(jug, clover)

    # 修改bingo_map, 检查能量溢出
    ret = 0
    if mark_result == 0:  # 罐子
        mark_count[0] += 1
        bingo_map[x][y] = 0
    elif mark_result == 1:  # 三叶草
        bingo_map[x][y] = -3
        for x_ in range(max(0, x - 1), min(4, x + 1) + 1):
            for y_ in range(max(0, y - 1), min(4, y + 1) + 1):
                point = bingo_map[x_][y_]
                if point == 0:
                    bingo_map[x_][y_] = 1
                elif point == 1:
                    bingo_map[x_][y_] = 0
                    ret += 1
                else:
                    pass
    elif mark_result == 2:  # 四叶草
        mark_count[1] += 1
        bingo_map[x][y] = -4
        for x_ in range(5):
            for y_ in range(5):
                point = bingo_map[x_][y_]
                if point == 0:
                    bingo_map[x_][y_] = 1
                elif point == 1:
                    bingo_map[x_][y_] = 0
                    ret += 1
                else:
                    pass
    else:  # 空
        bingo_map[x][y] = -2

    return ret


def one_play(bingo_count):
    bingo_map = [  # -4: 四叶草, -3: 三叶草, -2: 空, -1: 未被标记, 0: 空能量罐子, 1: 一半能量罐子
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    gold_count = 0  # 金币
    round_count = 0  # 轮数
    mark_count = [0, 0]  # 罐子计数, 四叶草计数
    rand_arr = get_rand_arr()
    for x, y in rand_arr:
        gold_add = one_mark(bingo_map, x, y, mark_count)
        gold_count += gold_add
        if gold_count >= Z:  # bingo
            for index in range(round_count, 25):
                bingo_count[index] += 1
            break
        round_count += 1
        # print 'x: {}, y: {}'.format(x, y)
        # pprint(bingo_map)
        # print '*' * 20


if __name__ == '__main__':
    bingo_count = [0 for i in range(25)]
    # one_play(bingo_count)
    # print bingo_count
    for i in range(10000):
        one_play(bingo_count)
    sleep(0.2)
    for ball, num in enumerate(bingo_count):
        print (ball + 1, num)

    # 折线图
    x = range(1, 26)
    y = bingo_count
    pl.plot(
        x, y,
        marker='o',
        linestyle='--',
        linewidth=2,
        markerfacecolor='m',
        color='b',
        label='bingo-balls'
    )
    pl.legend(loc='upper left')
    pl.xlabel('balls')
    pl.ylabel('bingo')
    pl.title('Clover.')
    pl.show()
