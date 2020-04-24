# coding=utf-8


class SensitiveInfo:
    # 希望保护的信息
    def __init__(self):
        self.users = ['nick', 'tom', 'ben']

    def read(self):
        print 'count: {}, list: {}'.format(len(self.users), ', '.join(self.users))

    def add(self, user):
        self.users.append(user)
        print 'Add user {}'.format(user)


class Info:
    def __init__(self):
        self.protected = SensitiveInfo()

    def read(self):
        self.protected.read()

    def add(self, user):
        self.protected.add(user)


if __name__ == '__main__':
    info = Info()
    while True:
        key = raw_input('1: read list, 2: add user, 3: quit ')
        if key == '1':
            info.read()
        elif key == '2':
            user = raw_input('input user name: ')
            info.add(user)
        elif key == '3':
            break
        else:
            print 'unknown option: {}'.format(key)
