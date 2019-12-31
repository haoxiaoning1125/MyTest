# coding=utf-8

import xlwt
import random

X_PRO = 0.6  # 1个篮子出2个食材的概率, 否则出3个
Y_PRO = 0.3  # 出1个篮子的概率, 否则出2个
FP = 1600    # 通关所需point

ING_PRO = [
    0.182, 0.117, 0.112, 0.056, 0.056,
    0.093, 0.089, 0.075, 0.056, 0.047,
    0.033, 0.042, 0.012, 0.016, 0.014
]
assert sum(ING_PRO) == 1.0
# print sum(ING_PRO)

FOOD = [
    [[(0, 1), (1, 1), (2, 2), (3, 2)], 15, 0.33],
    [[(0, 2), (1, 1), (4, 2), (5, 2)], 20, 0.47],
    [[(1, 1), (2, 3), (5, 2), (6, 2)], 25, 0.60],
    [[(0, 2), (1, 2), (6, 2), (7, 2), (8, 2)], 30, 0.80],
    [[(0, 2), (1, 1), (7, 2), (8, 2), (9, 3)], 40, 1.00],
    [[(0, 2), (7, 2), (9, 2), (10, 2), (11, 3)], 50, 1.27],
    [[(0, 3), (10, 3), (11, 3), (12, 3)], 60, 1.53],
    [[(0, 2), (1, 3), (6, 3), (13, 3), (14, 3)], 80, 1.87]
]


def random_weight_float(w):
    r = random.random()
    for i in range(len(w)):
        r -= w[i]
        if r <= 0:
            return i


def open_basket(s1, s2, y):
    """:param s1: 总食材统计, s2: 当前食材统计, y: 篮子个数"""
    for i in range(y):
        x = 2 if random.random() > 1 - X_PRO else 3
        for j in range(x):
            ing = random_weight_float(ING_PRO)
            s1[ing] += 1
            s2[ing] += 1


def cooked(s2, ing_need):
    for ing in ing_need:
        index = ing[0]
        num = ing[1]
        if s2[index] < num:
            return False
    return True


def check_food(s2):
    foods = []
    for f_index in range(8):
        ing_need = FOOD[f_index][0]
        if cooked(s2, ing_need):
            foods.append(f_index)
    if foods:
        return max(foods)
    else:
        return -1


def cook_food(s2, food_count):
    add_rp = 0
    add_rt = 0
    while True:
        food_index = check_food(s2)
        if food_index == -1:
            break
        food_count[food_index] += 1
        food_conf = FOOD[food_index]
        ing_use = food_conf[0]
        add_rp += food_conf[1]
        add_rt += food_conf[2]
        for i, n in ing_use:
            s2[i] -= n

    return add_rp, add_rt


def one_play():
    rp = 0  # 总积分
    rt = 0  # 奖励
    s1 = [0 for _ in range(15)]  # 总食材
    s2 = [0 for _ in range(15)]  # 当前食材
    n = 0  # 轮数
    food_count = [0 for _ in range(8)]  # food统计
    while rp < FP:
        n += 1
        y = 1 if random.random() > 1 - Y_PRO else 2
        open_basket(s1, s2, y)
        add_rp, add_rt = cook_food(s2, food_count)
        rp += add_rp
        rt += add_rt
    # print rp
    return [n, rt, food_count]


if __name__ == '__main__':
    # wb = xlwt.Workbook()
    # sheet = wb.add_sheet('sheet1')
    for i in range(100):
        n, rt, food_count = one_play()
        print n, rt, food_count
        # sheet.write(i, 0, str(n))
        # sheet.write(i, 1, str(s1))
        # sheet.write(i, 2, str(sum(s1)))
        # sheet.write(i, 3, str(s2))
        # sheet.write(i, 4, str(sum(s2)))
        # sheet.write(i, 5, str(rt))
    # wb.save('food.xls')
