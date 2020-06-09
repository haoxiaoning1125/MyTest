# coding=utf-8
# 梯子主题

import random
import pylab as pl
# from pprint import pprint


def bfs(start, matrix):  # start: [x, y]
    """广度优先遍历"""
    n = len(matrix)
    queue_ = [start]
    vis = [[False for y in range(n)] for x in range(n)]
    vis[start[0]][start[1]] = True
    # dires = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue_:
        x, y = queue_.pop(0)
        if matrix[x][y] == 3:
            dires = [[0, 1], [0, -1], [1, 0]]
        elif matrix[x][y] == 1:
            dires = [[0, 1], [0, -1]]
        else:
            dires = []
        for dx, dy in dires:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] in (1, 3):
                queue_.append([nx, ny])
                vis[nx][ny] = True
    return vis


def get_rand_arr():
    arr = [
        [i, j] for i in range(5) for j in range(5)
    ]
    random.shuffle(arr)
    return arr


def is_bingo(bingo_map):
    start_ladder_index = get_ladder_index_in_one_line(bingo_map, 0)
    end_ladder_index = get_ladder_index_in_one_line(bingo_map, 4)
    for start in start_ladder_index:
        vis = bfs(start, bingo_map)
        for end_x, end_y in end_ladder_index:
            if vis[end_x][end_y]:
                return True
    return False


def get_ladder_index(bingo_map):
    """获取未标记梯子的坐标"""
    ladder_index = []
    for x in range(5):
        for y in range(5):
            if bingo_map[x][y] == 2:
                ladder_index.append([x, y])
    return ladder_index


def get_ladder_index_in_one_line(bingo_map, line):
    """获取某一行已标记梯子的坐标"""
    final_ladder_index = []
    for y in range(5):
        if bingo_map[line][y] == 3:
            final_ladder_index.append([line, y])
    return final_ladder_index


def add_random_prop(bingo_map, prop_num):
    """添加随机道具"""
    unmark_index = []
    for x in range(5):
        for y in range(5):
            if bingo_map[x][y] == 0:
                unmark_index.append([x, y])
    random_index = random.sample(unmark_index, prop_num)
    for x, y in random_index:
        bingo_map[x][y] = 4


def one_play(bingo_count):
    bingo_map = [  # 0: 未标记, 1: 通路, 2: 未标记梯子, 3: 已标记梯子, 4: 未标记道具
        [2, 0, 0, 0, 2],
        [0, 2, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0],
        [2, 0, 0, 0, 2],
    ]

    # pprint(bingo_map)
    add_random_prop(bingo_map, 3)
    # pprint(bingo_map)

    ladder_index = get_ladder_index(bingo_map)
    round_num = 0
    rand_arr = get_rand_arr()
    for x, y in rand_arr:
        state = bingo_map[x][y]
        if state == 0:
            bingo_map[x][y] = 1
        elif state == 2:
            bingo_map[x][y] = 3
            ladder_index.remove([x, y])
        elif state == 4:
            bingo_map[x][y] = 1
            if ladder_index:
                x_, y_ = random.choice(ladder_index)
                bingo_map[x_][y_] = 3
                ladder_index.remove([x_, y_])
        if is_bingo(bingo_map):
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
    pl.title('Ladder.')
    pl.show()
