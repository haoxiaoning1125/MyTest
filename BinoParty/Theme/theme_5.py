# coding=utf-8
# 骰子主题

import pylab as pl
from time import sleep
import random


DICE_PRO = [0.6, 0.9, 1.0]
X = 10
Y = 20
Z = 150


def one_play(bingo_count):
    dices = []
    score = 0
    for ball in range(25):
        dice_num = random_dice_num()
        dices.extend([random.choice([1, 2, 3, 4, 5, 6]) for i in range(dice_num)])
        if len(dices) >= 3:
            three = dices[0:3]
            dices = dices[3:]
            score += get_socre(three)
            # print ball, score
            if score >= Z:  # bingo
                # bingo_count[balls] += 1
                for index in range(ball, 25):
                    bingo_count[index] += 1
                # print 'bingo'
                return
        # print score


def get_socre(three):
    score = 0
    three = sorted(three)
    if three[2] - three[1] == three[1] - three[0] == 1:
        score += X
    if three[0] == three[1] == three[2]:
        score += Y
    return score + sum(three)


def random_dice_num():
    a = random.random()
    for i, pro in enumerate(DICE_PRO):
        if a < pro:
            return i + 1
    return 3


if __name__ == '__main__':
    bingo_count = [0 for i in range(25)]
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
    pl.title('Monkey.')
    pl.show()
