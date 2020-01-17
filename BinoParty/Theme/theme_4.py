# coding=utf-8
# 猴子主题

import random
import pylab as pl
from tqdm import tqdm
from time import sleep


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
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] == 1:
                queue_.append([nx, ny])
                vis[nx][ny] = True
    return vis


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    arr.remove([1, 0])
    arr.remove([1, 4])
    random.shuffle(arr)
    return arr


def is_bingo(bingo_map):
    test_xys = [
        [0, 1], [0, 3]
    ]
    for x, y in test_xys:
        if bingo_map[x][y] == 1:
            vis = bfs([x, y], bingo_map)
            if True in vis[4]:
                return True
    return False


def one_play(bingo_count):
    bingo_map = [  # 0: 未标记, 1: 已标记, 2: 空白, 3: 香蕉
        [3, 0, 0, 0, 3],
        [2, 0, 0, 0, 2],
        [2, 0, 0, 0, 2],
        [2, 0, 0, 0, 2],
        [2, 0, 0, 0, 2]
    ]
    xys = get_rand_arr()
    balls = 0
    for x, y in xys:
        if bingo_map[x][y] == 0:
            bingo_map[x][y] = 1
        if is_bingo(bingo_map):
            # bingo_count[balls] += 1
            for index in range(balls, 23):
                bingo_count[index] += 1
            break
        balls += 1


if __name__ == '__main__':
    bingo_count = [0 for i in range(23)]
    for i in tqdm(range(10000)):
        one_play(bingo_count)

    sleep(0.2)
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
    pl.title('Monkey.')
    pl.show()
