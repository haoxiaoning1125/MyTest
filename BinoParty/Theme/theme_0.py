# coding=utf-8

import random
# from pprint import pprint


BINGO_MAP_CONFIG = [
    [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0]
    ],
    [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ],
    [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ],
    [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ],
    [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ],
    [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],

        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ],
]

BINGO_INDEX_CONFIG = []
for b_map in BINGO_MAP_CONFIG:
    index_add = []
    for x in range(5):
        for y in range(5):
            if b_map[x][y] == 1:
                index_add.append([x, y])
    if index_add:
        BINGO_INDEX_CONFIG.append(index_add)


def gen_bingo_map():
    ball_list = random.sample(range(1, 76), 25)
    return [
        ball_list[0:5],
        ball_list[5:10],
        ball_list[10:15],
        ball_list[15:20],
        ball_list[20:25]
    ]


def get_rand_arr():
    rand_arr = range(1, 76)
    random.shuffle(rand_arr)
    return rand_arr


def bingo_mark(bingo_map, num):
    """标记后, 记为100"""
    for x in range(5):
        for y in range(5):
            if bingo_map[x][y] == num:
                bingo_map[x][y] = 100


def is_bingo(bingo_map):
    for check_index in BINGO_INDEX_CONFIG:
        a_bingo = True
        for x, y in check_index:
            if bingo_map[x][y] != 100:
                a_bingo = False
                break
        if a_bingo:
            return True
    return False


def one_play(bingo_count):
    bingo_map = gen_bingo_map()
    bingo_map[2][2] = 100
    rand_arr = get_rand_arr()
    round_num = 0

    for num in rand_arr:
        bingo_mark(bingo_map, num)
        if is_bingo(bingo_map):
            bingo_count[round_num] += 1
            break
        round_num += 1


if __name__ == '__main__':
    bingo_count = [0 for i in range(75)]
    for i in range(1000):
        one_play(bingo_count)
    # print bingo_count
    print '01-10: {}'.format(sum(bingo_count[0:10]))
    print '11-20: {}, {}'.format(sum(bingo_count[10:20]), sum(bingo_count[0:20]))
    print '21-30: {}, {}'.format(sum(bingo_count[20:30]), sum(bingo_count[0:30]))
    print '31-40: {}, {}'.format(sum(bingo_count[30:40]), sum(bingo_count[0:40]))
    print '41-50: {}, {}'.format(sum(bingo_count[40:50]), sum(bingo_count[0:50]))
    print '51-60: {}, {}'.format(sum(bingo_count[50:60]), sum(bingo_count[0:60]))
    print '61-70: {}, {}'.format(sum(bingo_count[60:70]), sum(bingo_count[0:70]))
    print '71+: {}, {}'.format(sum(bingo_count[70:]), sum(bingo_count))
    print 'all_bingo: {}'.format(sum(bingo_count))
    average = 0
    for index, count in enumerate(bingo_count):
        average += (index + 1) * count / 1000.0
    print 'average: {}'.format(average)
