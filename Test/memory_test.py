# coding=utf-8

from memory_profiler import profile


@profile(precision=5)
def func1(length):
    for i in range(length):
        pass


@profile(precision=5)
def func2(length):
    for i in xrange(length):
        pass


if __name__ == '__main__':
    length = 10000
    func1(length)
    func2(length)
