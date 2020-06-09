# coding=utf-8

import random
import pylab as pl
# from pprint import pprint


def bfs(start, bingo_map, ladder_map):  # start: [x, y]
    """广度优先遍历"""
    n = len(bingo_map)
    queue_ = [start]
    vis = [[False for y in range(n)] for x in range(n)]
    vis[start[0]][start[1]] = True
    dires = [[0, 1], [0, -1]]
    while queue_:
        x, y = queue_.pop(0)
        for dx, dy in dires:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and bingo_map[nx][ny] == 1:
                queue_.append([nx, ny])
                vis[nx][ny] = True
        if (x, y) in ladder_map:
            nx, ny = ladder_map[(x, y)]
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and bingo_map[nx][ny] == 1:
                queue_.append([nx, ny])
                vis[nx][ny] = True
    return vis


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    arr.remove([4, 2])
    random.shuffle(arr)
    return arr


def is_bingo(bingo_map, ladder_map):
    start = [4, 2]
    ends = [[0, 0], [0, 4]]
    vis = bfs(start, bingo_map, ladder_map)
    # pprint(vis)
    for end in ends:
        if vis[end[0]][end[1]]:
            return True
    return False


def one_play(bingo_count):
    bingo_map = [  # 0: 未标记, 1: 已标记
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    ladder_map = {  # start: end
        (4, 0): [3, 0],
        (3, 2): [2, 2],
        (2, 0): [1, 0],
        (1, 2): [0, 2],
        (3, 1): [1, 1],
        (2, 1): [1, 1],
        (3, 1): [1, 1],
    }
    rand_arr = get_rand_arr()
    round_num = 0
    for x, y in rand_arr:
        bingo_map[x][y] = 1
        if is_bingo(bingo_map, ladder_map):
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
    pl.title('Ladder.')
    pl.show()
