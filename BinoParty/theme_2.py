# coding=utf-8

import random
from pylab import plt

I, J, K = 3, 5, 7
X, P, Y = 0.05, 0.01, 0.8
CARDS_NUM = [I, J, K]
N = 20


def is_bingo(pokers):
    if pokers == [13, 13, 13, 13]:
        return True
    return False


def deal_pokers(pokers, joker_lev):
    cards_num = CARDS_NUM[joker_lev]
    cn = [13 - i for i in pokers]
    indexs = [0] * cn[0] + [1] * cn[1] + [2] * cn[2] + [3] * cn[3]
    indexs_add = random.sample(indexs, cards_num) if len(indexs) > cards_num else indexs
    for i in indexs_add:
        pokers[i] += 1


def get_joker(joker_lev, n):
    if joker_lev == 2:
        return 0
    else:
        p = X + n * P
        if random.random() > 1 - p:
            return 1
        return 0


def one_play(ret_dict):
    joker_lev = 0
    pokers = [0, 0, 0, 0]
    n1, n2 = 0, 0
    for i in range(25):
        n1 += 1
        n2 += 1

        jl_add = get_joker(joker_lev, n1)
        joker_lev += jl_add
        if jl_add:
            n1 = 0
        else:
            yy = Y if n2 < N else 1
            if random.random() > 1 - yy:
                deal_pokers(pokers, joker_lev)
        # print joker_lev
        # print pokers
        if is_bingo(pokers):
            ret_dict[i] += 1
            # break


if __name__ == '__main__':
    ret_dict = [0 for i in range(25)]
    for i in range(10000):
        one_play(ret_dict)
    for i, num in enumerate(ret_dict):
        print(i + 1, num)

    # 折线图
    x = range(1, 26)
    y = ret_dict
    plt.plot(x, y, 'ro-', color='#4169E1', alpha=0.8)
    plt.legend(loc='upper right')
    plt.xlabel('ball')
    plt.ylabel('bingo')
    plt.show()
