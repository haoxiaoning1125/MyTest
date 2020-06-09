# coding=utf-8
# 矿工

import random
import pylab as pl
# from pprint import pprint


def bfs(start, matrix):  # start: [x, y]
    n = len(matrix)
    queue_ = [start]
    vis = [[False for y in range(n)] for x in range(n)]
    vis[start[0]][start[1]] = True
    dires = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue_:
        x, y = queue_.pop(0)
        for dx, dy in dires:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] == 4:
                queue_.append([nx, ny])
                vis[nx][ny] = True
    return vis


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    arr.remove([0, 2])
    random.shuffle(arr)
    return arr


def is_bingo(bingo_map):
    vis = bfs([0, 2], bingo_map)
    return vis[4][0] or vis[4][2] or vis[4][4]


def small_boom(bingo_map, x, y):
    bingo_map[x][y] = 4
    dxy = [[-1, 0], [1, 0]]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            state = bingo_map[nx][ny]
            bingo_map[nx][ny] = 4
            if state == 2:
                small_boom(bingo_map, nx, ny)
            elif state == 3:
                big_boom(bingo_map, nx, ny)


def big_boom(bingo_map, x, y):
    bingo_map[x][y] = 4
    dxy = [[0, -1], [0, 1]]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            state = bingo_map[nx][ny]
            bingo_map[nx][ny] = 4
            if state == 2:
                small_boom(bingo_map, nx, ny)
            elif state == 3:
                big_boom(bingo_map, nx, ny)


def one_play(bingo_count):
    bingo_map = [  # 0: 空格, 1: 石头, 2: 小炸弹, 3: 大炸弹, 4: 已标记, 9: 门
        [0, 0, 4, 0, 0],
        [1, 2, 1, 0, 1],
        [0, 0, 1, 3, 2],
        [0, 1, 0, 1, 1],
        [9, 0, 9, 0, 9],
    ]

    rand_arr = get_rand_arr()
    round_num = 0
    for x, y in rand_arr:
        state = bingo_map[x][y]
        if state == 0 or state == 9:
            bingo_map[x][y] = 4
        elif state == 2:
            small_boom(bingo_map, x, y)
        elif state == 3:
            big_boom(bingo_map, x, y)
        else:
            pass
        if is_bingo(bingo_map):
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
    pl.title('Miner.')
    pl.show()
