# coding=utf-8
# Sleep Beauty

import random
import pylab as pl

X = 0.6  # 出道具


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
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] == 0:
                queue_.append([nx, ny])
                vis[nx][ny] = True
    return vis


def is_bingo(bingo_map):
    start = [1, 2]
    vis = bfs(start, bingo_map)
    return True in vis[4]


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    arr.remove([1, 2])
    random.shuffle(arr)
    return arr


def cut_down(bingomap):
    xys = []
    for i in range(5):
        for j in range(5):
            if bingomap[i][j] == 1:
                xys.append([i, j])
    if len(xys) >= 1:
        xys = random.sample(xys, 1)
        for x, y in xys:
            bingomap[x][y] = 0
        return True
    else:
        return False


def count_2(bingomap):
    count = 0
    for i in range(5):
        for j in range(5):
            if bingomap[i][j] == 2:
                count += 1
    return count


def one_play(bingo_count):
    bingo_map = [  # 0: 通路, 1: 荆棘, 2: 未标记, 4: 未标记荆棘
        [2, 2, 2, 2, 2],
        [2, 4, 0, 4, 2],
        [2, 2, 4, 2, 2],
        [4, 2, 4, 2, 4],
        [2, 4, 4, 4, 2]
    ]
    # chopper = 0
    xys = get_rand_arr()
    balls = 0
    bingo_flag = False
    for x, y in xys:
        if bingo_flag:
            bingo_count[balls] += 1
            balls += 1
            continue
            # break
        state = bingo_map[x][y]
        if state == 2:
            bingo_map[x][y] = 0
            if count_2(bingo_map) <= 3:
                chopper = 1
            else:
                chopper = 1 if random.random() > 1 - X else 0  # 特殊道具
            if chopper:
                cut_down(bingo_map)
            # chopper = 0
        elif state == 4:
            bingo_map[x][y] = 1
        if is_bingo(bingo_map):
            bingo_count[balls] += 1
            bingo_flag = True
        balls += 1


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
    pl.title('Sleep Beauty.')
    pl.show()
