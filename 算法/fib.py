# coding=utf-8
import time


def fib_1(n):
    if n < 2:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    fib = [1, 1]
    for i in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


if __name__ == '__main__':
    t1 = time.time()
    print fib_1(30)
    t2 = time.time()
    print fib_2(30)
    t3 = time.time()
    print t2 - t1
    print t3 - t2
