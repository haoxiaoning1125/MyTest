# coding=utf-8

import random
import pylab as pl

X = 0.5
A = 0.33
B = 0.33
K = 4
L = 5

PEAS_INDEX = [0, 1, 2, 3, 4]


def get_rand_arr():
    a = range(25)
    random.shuffle(a)
    return a


def is_bingo(zombies):
    return zombies.count(0) >= L


def random_sun(sun_pro):
    r = random.random()
    for index, num in enumerate(sun_pro):
        r -= num
        if r < 0:
            return index + 1
    return len(sun_pro)


def peas_lev_up(peas, num):
    indexs = random.sample(PEAS_INDEX, num)
    for index in indexs:
        peas[index] = 1
    return indexs


def shoot(peas, zombies, num, two=0):
    blood = zombies[num]
    if two:
        zombies[num] = max(blood - 2, 0)
    else:
        zombies[num] = max(blood - 2 if peas[num] else blood - 1, 0)


def one_play(bingo_count):
    round_num = 0
    rand_arr = get_rand_arr()
    zombies = [K for _ in range(5)]
    peas = [0, 0, 0, 0, 0]  # 0: 未升级, 1: 已升级
    suns = [0, 0, 0, 0, 0]
    for arr in rand_arr:
        peas_count = sum(peas)
        index = arr % 5
        if peas_count <= 2:
            if not suns[index]:
                r = random.random()
                if r < X:  # sun
                    sun = random_sun([A, B, 1 - A - B])
                    indexs = peas_lev_up(peas, sun)
                    suns[index] = 1
                    for index in indexs:
                        shoot(peas, zombies, index)
                else:  # shoot
                    shoot(peas, zombies, index)
            else:
                shoot(peas, zombies, index)
        elif peas_count == 3:
            if not suns[index]:
                r = random.random()
                if r < X:  # sun
                    sun = random_sun([A, 1 - A])
                    indexs = peas_lev_up(peas, sun)
                    suns[index] = 1
                    for index in indexs:
                        shoot(peas, zombies, index)
                else:  # shoot
                    shoot(peas, zombies, index)
            else:
                shoot(peas, zombies, index)
        elif peas_count == 4:
            if not suns[index]:
                r = random.random()
                if r < X:  # sun
                    sun = 1
                    indexs = peas_lev_up(peas, sun)
                    suns[index] = 1
                    for index in indexs:
                        shoot(peas, zombies, index)
                else:  # shoot
                    shoot(peas, zombies, index)
            else:
                shoot(peas, zombies, index)
        else:
            shoot(peas, zombies, arr % 5)
        if is_bingo(zombies):
            for index in range(round_num, len(bingo_count)):
                bingo_count[index] += 1
            break
        round_num += 1


if __name__ == '__main__':
    bingo_count = [0 for i in range(25)]
    for i in range(10000):
        one_play(bingo_count)

    for i, n in enumerate(bingo_count):
        print (i + 1, n)

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
    # pl.axis([0, 25, -1000, 11000])
    pl.legend(loc='upper left')
    pl.xlabel('balls')
    pl.ylabel('bingo')
    pl.title('FathersDay.')
    pl.show()
