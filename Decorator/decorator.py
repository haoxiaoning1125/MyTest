# coding=utf-8
# 带参数的装饰器
# 装饰器在被装饰的函数定义之后立刻执行, 通常在python导入(加载模块)时

import time


def time_of(parastate=0):
    def inner1(func):
        def inner2(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            para = []
            if parastate:
                para.extend(locals()['args'])
                for k, v in locals()['kwargs'].items():
                    para.append('{}={}'.format(k, v))
            print 'func: {}{}, time used: {}'.format(func.__name__, tuple(para), end - start)
            return ret
        return inner2
    return inner1


@time_of(parastate=1)
def add_(a, b):
    time.sleep(0.2)
    return a + b


if __name__ == '__main__':
    print add_(100, 100)
    print add_(a=200, b=200)
    print add_(300, b=300)
