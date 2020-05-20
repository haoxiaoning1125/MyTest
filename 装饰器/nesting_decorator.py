# coding=utf-8
# 嵌套装饰器, nesting_decorator

import time


def time_count(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print 'time used: {}'.format(end - start)
        return ret
    return inner


def para_check_int(func):
    def inner(*args, **kwargs):
        for num in list(args) + kwargs.values():
            if not isinstance(num, int):
                print 'para {} is not int'.format(num)
                return -1
        print 'paras are all int'
        return func(*args, **kwargs)
    return inner


# add = para_check_int(time_count(add))
@para_check_int
@time_count
def add(a, b):
    time.sleep(0.2)
    return a + b


if __name__ == '__main__':
    print add(1, 2)
    print add(1, '2')
    print add(a=1, b='2')
