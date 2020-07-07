# coding=utf-8

import commands
import time
from controllers.family import *

user_point_days = dict()  # uid: [one_day, total]
# family_points = dict()  # family_id: points
DAILYTASK_FAMILY_CHEST_ADD = [15, 25, 40, 50, 50, 0, 0, 0]


def update_user_point(file_name):
    user_point_one_day = dict()  # uid: task_lev
    cmd = 'grep bingo_themetask6_reward /home/ubuntu/scribe-log/newbingo.request.time/{} | cut -f 2'.format(file_name)
    uids_str = commands.getoutput(cmd)
    uids = uids_str.split('\n')
    for uid in uids:
        if uid in user_point_one_day:
            user_point_one_day[uid] += 1
        else:
            user_point_one_day[uid] = 1

    # print user_point_one_day
    for uid, lev in user_point_one_day.items():
        user_point_one_day[uid] = sum(DAILYTASK_FAMILY_CHEST_ADD[0:lev])
    return user_point_one_day


FILES = ['newbingo.request.time-2020-06-26_00000',
         'newbingo.request.time-2020-06-27_00000',
         'newbingo.request.time-2020-06-28_00000']
three_days = dict()

for file_name in FILES:
    one_day = update_user_point(file_name)
    for uid, points in one_day.items():
        if uid in three_days:
            three_days[uid] += points
        else:
            three_days[uid] = points

result = dict()
count = 0
for uid, points in three_days.items():
    family_user = BingoFamilyUser.get(uid)
    if family_user:
        family_id = family_user.family_id
        if family_id in result:
            result[family_id] += points
        else:
            result[family_id] = points
    count += 1
    if count % 1000 == 0:
        # print count
        time.sleep(10)

for family_id, points in result.items():
    print family_id, points

