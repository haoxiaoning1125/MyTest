# coding=utf-8
# 装饰器

import time


def time_of(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        para = []
        para.extend(locals()['args'])
        for k, v in locals()['kwargs'].items():
            para.append('{}={}'.format(k, v))
        print 'func: {}{}, time used: {}'.format(func.__name__, tuple(para), end - start)
        return ret
    return inner


@ time_of
def add_(a, b):
    time.sleep(0.2)
    return a + b


if __name__ == '__main__':
    print add_(100, 100)
    print add_(a=200, b=200)
    print add_(300, b=300)
