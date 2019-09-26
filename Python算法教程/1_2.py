# coding=utf-8

import time


def time_of(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print end - start
    return inner


@time_of
def func1(num):
    nums = []
    for i in xrange(num):
        nums.append(i)
    nums.reverse()


@time_of
def func2(num):
    nums = []
    for i in xrange(num):
        nums.insert(0, i)


if __name__ == '__main__':
    num = 10 ** 5
    func1(num)
    func2(num)
