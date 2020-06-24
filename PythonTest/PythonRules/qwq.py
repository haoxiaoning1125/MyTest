# coding=utf-8
# 两份旅游名单, 找出同时去过两地的人
# 姓名和电话号码完全相同, 视为同一个人

USERS_PT = [
    {'name': 'A', 'tel': 1000, 'time': '2010-10-01'},
    {'name': 'B', 'tel': 2000, 'time': '2012-11-19'},
    {'name': 'C', 'tel': 3000, 'time': '2014-02-05'},
    {'name': 'D', 'tel': 4000, 'time': '2019-12-13'},
]
USERS_NZ = [
    {'name': 'C', 'tel': 3000, 'time': '2009-10-31'},
    {'name': 'D', 'tel': 5000, 'time': '2020-04-03'},
    {'name': 'E', 'tel': 6000, 'time': '2001-07-21'},
    {'name': 'F', 'tel': 7000, 'time': '2013-09-02'},
]

# https://cloud.tencent.com/developer/article/1462518
