# coding=utf-8
# 任务: 保持递归函数与朴素版本的一样简单, 但在性能上又能与使用memoization的函数相近

import functools


def memoize(fn):
    known = dict()

    # @functools.wraps(fn)  # 将原函数对象的指定属性复制给包装函数对象, 默认有 module、name、doc
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize  # fibonacci = memoize(fibonacci)
def fibonacci(n):
    assert n >= 0, 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def sum_n(n):
    assert n >= 0, 'n must be >= 0'
    return 0 if n == 0 else sum_n(n - 1) + n


if __name__ == '__main__':
    print fibonacci(325)
    print sum_n(100)
