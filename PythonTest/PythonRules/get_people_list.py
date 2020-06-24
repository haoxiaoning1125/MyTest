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


class User:
    def __init__(self, name, tel, time):
        self.name = name
        self.tel = tel
        self.time = time

    def __hash__(self):
        return hash((self.name, self.tel))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        return 'name: {}, tel: {}, time: {}'.format(self.name, self.tel, self.time)


def gen_user_set(user_list):
    ret = set()
    for user in user_list:
        ret_user = User(user['name'], user['tel'], user['time'])
        ret.add(ret_user)
    return ret


if __name__ == '__main__':
    user_pt = gen_user_set(USERS_PT)
    user_nz = gen_user_set(USERS_NZ)
    diff = user_pt & user_nz
    for user in diff:
        print user
