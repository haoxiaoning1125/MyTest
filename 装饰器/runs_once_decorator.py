# coding=utf-8
# 只允许函数被执行一次的装饰器


class RunsOnce:
    def __init__(self):
        self.runs_count = 0

    def runs_once(self, func):
        def inner(*args, **kwargs):
            if self.runs_count < 1:
                self.runs_count += 1
                return func(*args, **kwargs)
            else:
                print 'func {} can only run once.'.format(func.__name__)
                return None
        return inner


def runs_once_decorator(func):
    ro = RunsOnce()
    return ro.runs_once(func)


@runs_once_decorator
def add(a, b):
    print '{} + {} = {}'.format(a, b, a + b)


@runs_once_decorator
def sub(a, b):
    print '{} - {} = {}'.format(a, b, a - b)


if __name__ == '__main__':
    add(1, 1)
    add(2, 2)
    sub(1, 1)
    sub(2, 2)
