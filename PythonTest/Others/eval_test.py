# coding=utf-8
# 动态函数调用


def add(a, b):
    return a + b


if __name__ == '__main__':
    print eval('add')(1, 2)

    args = [1, 2]
    kwargs = {}
    print eval('add')(*args, **kwargs)
