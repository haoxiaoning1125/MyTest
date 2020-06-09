# coding=utf-8
# 切水果

import random
import pylab as pl
# from pprint import pprint


APPLE_COUNT = 8
PINEAPPLE_COUNT = 8
WATERMELON_COUNT = 9

DIRES_LIST = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    random.shuffle(arr)
    return arr


def random_one_fruit(fruits_count):
    for index, num in enumerate(fruits_count):
        if num < 6:
            fruits_count[index] += 1
            return index + 1
    ret = random.choice([1, 2, 3])
    fruits_count[ret - 1] += 1
    return ret


def random_fruits(bingo_map):
    fruits_list = [1 for i in range(APPLE_COUNT)] + \
                  [2 for i in range(PINEAPPLE_COUNT)] + \
                  [3 for i in range(WATERMELON_COUNT)]
    random.shuffle(fruits_list)
    for x in range(5):
        for y in range(5):
            bingo_map[x][y] = fruits_list.pop(0)
    

def cut_fruit(bingo_map, x, y, knife_type, final, fruits_count):
    if 4 <= knife_type <= 7:
        dires = [DIRES_LIST[knife_type - 4]]
    else:
        dires = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    state = bingo_map[x][y]
    final[state - 1] += 1
    fruits_count[state - 1] -= 1
    bingo_map[x][y] = random_one_fruit(fruits_count)
    if 1 <= state <= 3:
        final[state - 1] += 1
        fruits_count[state - 1] -= 1
        bingo_map[x][y] = random_one_fruit(fruits_count)
    for dx, dy in dires:
        nx, ny = x + dx, y + dy
        while 0 <= nx <= 4 and 0 <= ny <= 4:
            state = bingo_map[nx][ny]
            if 1 <= state <= 3:
                final[state - 1] += 1
                fruits_count[state - 1] -= 1
                bingo_map[nx][ny] = random_one_fruit(fruits_count)
            nx, ny = nx + dx, ny + dy


def one_play(bingo_count):
    bingo_map = [  # 0: 空位, 1: 苹果, 2: 菠萝, 3: 西瓜
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    random_fruits(bingo_map)
    fruits_count = [8, 8, 9]
    knife_map = {  # 4: 上, 5: 下, 6: 左, 7: 右, 8: 双刀
        (0, 0): 5,
        (1, 1): 8,
        (2, 3): 8,
        (3, 4): 6,
        (4, 1): 7
    }

    round_num = 0
    final = [0, 0, 0]

    rand_arr = get_rand_arr()
    for x, y in rand_arr:
        state = bingo_map[x][y]
        if 1 <= state <= 3:
            final[state - 1] += 1
            fruits_count[state - 1] -= 1
            bingo_map[x][y] = random_one_fruit(fruits_count)
        if (x, y) in knife_map:
            cut_fruit(bingo_map, x, y, knife_map[(x, y)], final, fruits_count)
        if final[0] >= 10 and final[1] >= 10 and final[2] >= 10:
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
    pl.title('CutFruits.')
    pl.show()
