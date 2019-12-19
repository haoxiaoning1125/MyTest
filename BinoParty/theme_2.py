# coding=utf-8

import random
# from pylab import plt
import pylab as plt

I, J, K = 3, 4, 6
X, P, Y = 0.05, 0.02, 1
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
    return len(indexs_add)


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
    cards_count = 0
    for i in range(25):
        n1 += 1
        n2 += 1
        jl_add = get_joker(joker_lev, n1)
        if jl_add:
            joker_lev += jl_add
            n1 = 0
            cards_count += 1
        else:
            yy = 1 if I * (22 - n2) <= 52 - cards_count else Y  # 保底
            if random.random() >= 1 - yy:
                cards_count += deal_pokers(pokers, joker_lev)
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
    plt.plot(
        x, y,
        marker='o',
        linestyle='--',
        color='b',
        markerfacecolor='m',
        alpha=0.8,
    )
    # plt.axis([0, 25, -1000, 11000])
    plt.legend(loc='upper left')
    plt.title('solitaire')
    plt.xlabel('ball')
    plt.ylabel('bingo')
    plt.show()
