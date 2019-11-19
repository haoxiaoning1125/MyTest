# coding=utf-8
# timeit
# 函数命名使用test会触发test模式...

from timeit import Timer, timeit, repeat


def func_1():
    n = 0
    for i in range(101):
        n += i
    return n


def func_2():
    return sum(range(101))


def func_3():
    return sum([i for i in range(101)])


if __name__ == '__main__':
    t1 = Timer("func_1()", "from __main__ import func_1")
    t2 = Timer("func_2()", "from __main__ import func_2")
    t3 = Timer("func_3()", "from __main__ import func_3")

    print t1.timeit(10000)
    print t2.timeit(10000)
    print t3.timeit(10000)
    print '-' * 20

    print t1.repeat(3, 10000)
    print t2.repeat(3, 10000)
    print t3.repeat(3, 10000)
    print '-' * 20

    print timeit(stmt=func_1, setup='from __main__ import func_1', number=10000)
    print timeit(stmt=func_2, setup='from __main__ import func_2', number=10000)
    print timeit(stmt=func_3, setup='from __main__ import func_3', number=10000)
    print '-' * 20

    print repeat(stmt=func_1, setup='from __main__ import func_1', number=10000, repeat=3)
    print repeat(stmt=func_2, setup='from __main__ import func_2', number=10000, repeat=3)
    print repeat(stmt=func_3, setup='from __main__ import func_3', number=10000, repeat=3)
    print '-' * 20
