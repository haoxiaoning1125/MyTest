# coding=utf-8
# methodcaller: 通过函数名字符串调用函数
# 状态机

from operator import methodcaller


class A():
    def func1(self):
        return 1

    def func2(self):
        return 2


if __name__ == '__main__':
    a = A()
    fnames = ['func1', 'func2']
    for f in fnames:
        if hasattr(a, f):
            print methodcaller(f)(a)
