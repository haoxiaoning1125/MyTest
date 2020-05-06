# coding=utf-8

import random
import pylab as pl


def bfs(start, bingo_map, holes):  # start: [x, y], holes:[[x, y],]已标记窟窿坐标
    n = len(bingo_map)
    queue_ = [start]
    vis = [[False for y in range(n)] for x in range(n)]
    vis[start[0]][start[1]] = True
    dires = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue_:
        x, y = queue_.pop(0)
        for dx, dy in dires:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and bingo_map[nx][ny] == 1:
                queue_.append([nx, ny])
                vis[nx][ny] = True
        if [x, y] in holes:
            holes.remove([x, y])
            for hole in holes:
                queue_.append(hole)
                vis[hole[0]][hole[1]] = True
    return vis


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    arr.remove([0, 0])
    arr.remove([4, 4])
    random.shuffle(arr)
    return arr


def is_bingo(bingo_map, holes):
    vis = bfs([0, 0], bingo_map, holes)
    return vis[4][4]


def one_play(bingo_count):
    bingo_map = [  # 0: 未标记, 1: 已标记, 2: 未标记窟窿, 3: 冰山
        [1, 0, 0, 3, 0],
        [0, 2, 0, 2, 0],
        [0, 3, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 0, 1],
    ]
    holes = []
    balls = 0
    for x, y in get_rand_arr():
        state = bingo_map[x][y]
        if state == 0:
            bingo_map[x][y] = 1
        elif state == 2:
            holes.append([x, y])
            bingo_map[x][y] = 1
        else:
            pass

        if is_bingo(bingo_map, holes):
            bingo_count[balls] += 1

        balls += 1


if __name__ == '__main__':
    bingo_count = [0 for _ in range(23)]
    for i in range(10000):
        one_play(bingo_count)

    for ball, num in enumerate(bingo_count):
        print (ball + 1, num)

    # 折线图
    x = range(1, 24)
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
    pl.title('Penguin.')
    pl.show()
