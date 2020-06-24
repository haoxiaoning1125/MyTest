# coding=utf-8
# 父亲节

import random
import pylab as pl
import importlib
from pprint import pprint

TOYS_NEED = 3
FATHER_PRO = 0.5


def bfs(start, matrix):  # start: [x, y]
    """广度优先遍历"""
    n = len(matrix)
    queue_ = [start]
    vis = [[False for y in range(n)] for x in range(n)]
    vis[start[0]][start[1]] = True
    dires = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue_:
        x, y = queue_.pop(0)
        for dx, dy in dires:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] in (2, 4):
                queue_.append([nx, ny])
                vis[nx][ny] = True
    return vis


def is_bingo(bingo_map, toys_position):
    vis = bfs([4, 2], bingo_map)
    toys_count = 0
    for x, y in toys_position:
        if vis[x][y]:
            toys_count += 1
    return toys_count >= TOYS_NEED


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    arr.remove([4, 2])
    random.shuffle(arr)
    return arr


def random_toys(bingo_map):
    rand_arr = get_rand_arr()
    remove_p = [[3, 1], [3, 2], [3, 3], [4, 1], [4, 3]]
    for p in remove_p:
        rand_arr.remove(p)
    ps = random.sample(rand_arr, 5)
    for px, py in ps:
        bingo_map[px][py] = 3
    return ps


def move_toys(bingo_map, x, y):
    rand = random.randint
    if rand < FATHER_PRO:
        if bingo_map[x][y] not in (3, 4):
            dxy = [[1, 0], [-1, 0]]  # 下, 上
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= 4 and 0 <= ny <= 4:
                    if bingo_map[nx][ny] == 3:
                        bingo_map[x][y] = 4
                        bingo_map[nx][ny] = 2
                        return True
    return False


def one_play(bingo_count):
    bingo_map = [  # 0, 1: 未标记, 2: 已标记, 3: 未标记玩具, 4: 已标记玩具
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 2, 1, 0],
    ]
    toys_position = random_toys(bingo_map)
    rand_arr = get_rand_arr()
    round_num = 0
    last_move_round = 0
    for x, y in rand_arr:
        if last_move_round + 1 != round_num:
            move_flag = move_toys(bingo_map, x, y)
            if move_flag:
                last_move_round = round_num
        state = bingo_map[x][y]
        if state < 2:
            bingo_map[x][y] = 2
        elif state == 3:
            bingo_map[x][y] = 4

        if is_bingo(bingo_map, toys_position):
            for index in range(round_num, len(bingo_count)):
                bingo_count[index] += 1
            break

        round_num += 1


if __name__ == '__main__':
    bingo_count = [0 for i in range(24)]
    for i in range(10000):
        one_play(bingo_count)
    for i, n in enumerate(bingo_count):
        print (i + 1, n)

    x = range(1, 25)
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
