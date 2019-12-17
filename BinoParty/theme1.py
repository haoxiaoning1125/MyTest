# coding=utf-8

import random
from pylab import plt

RANDOM_Y_ORP = 0.12  # 出 y - 1 的概率


def get_rand_arr():
    a = [i for i in range(25)]
    random.shuffle(a)
    return a


def get_random_y(y):
    if random.random() > RANDOM_Y_ORP:
        return y
    return y - 1


def boom_1(bingo_map, start, y):
    """带星星标记的格子被标记, 分裂出y个星星"""
    indexs = []
    for i, num in enumerate(bingo_map):
        if num != -1 and i != start:
            indexs.append(i)
    if indexs:
        index_l = []
        for i in range(get_random_y(y)):
            index_l.append(random.choice(indexs))

        # if len(indexs) >= y:
        #     indexs = random.sample(indexs, y)  # ？？？？
        # print index_l
        for index in index_l:
            bingo_map[index] += 1
    bingo_map[start] = -1


def boom_2(bingo_map, y, z):
    """z个星星标记后, 分裂出y个星星"""
    indexs = []
    for i in range(len(bingo_map)):
        if bingo_map[i] >= z:
            indexs.append(i)
    for index in indexs:
        boom_1(bingo_map, index, y)
    # print bingo_map


def is_bingo(bingo_map):
    if bingo_map != [-1 for _ in range(25)]:
        return False
    return True


def one_play(ret_dic, x, y, z):
    bingo_map = [0 for i in range(25 - x)] + [1 for i in range(x)]  # -1: 消除, 0+: 星星个数
    random.shuffle(bingo_map)

    rand_arr = get_rand_arr()

    for ball in range(25):  # 读球个数
        arr = rand_arr[0: ball + 1]  # 被标记的下标
        # print arr
        # print bingo_map
        for i, star in enumerate(bingo_map):
            if star > 0 and i in arr:  # 带星星标记的格子被标记, 分裂y个星星
                boom_1(bingo_map, i, y)
        # z个星星标记后, 分裂出y个星星
        boom_2(bingo_map, y, z)
        if arr:
            bingo_map[arr[-1]] = -1
        if is_bingo(bingo_map):
            ret_dic[ball] += 1
            # return


if __name__ == '__main__':
    ret_dic = [0 for i in range(25)]
    x, y, z = 4, 2, 2

    for i in range(10000):
        one_play(ret_dic, x, y, z)

    # print ret_dic
    for i, num in enumerate(ret_dic):
        print(i + 1, num)

    # 折线图
    x = range(25)
    y = ret_dic
    plt.plot(x, y, 'ro-', color='#4169E1', alpha=0.8)
    plt.legend(loc='upper right')
    plt.xlabel('ball')
    plt.ylabel('bingo')
    plt.show()
