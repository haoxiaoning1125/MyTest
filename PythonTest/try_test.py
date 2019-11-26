# coding=utf-8
# try... except... else... finally...
# 没有异常产生, 执行else
# 无论如何都要执行finally
# 不要在try和except里return

import sys


def func1():
    try:
        print 1
    except Exception as e:
        print e
    else:
        print 2


def func2():
    try:
        a = 1 / 0
        print 1
    except Exception as e:
        print e
    else:
        print 2


def func3():
    try:
        a = 1
        return
    except Exception as e:
        print e
    finally:
        print 233


def func4():
    try:
        a = 1
        sys.exit(0)
    except Exception as e:
        print e
    finally:
        print 233


if __name__ == '__main__':
    func_names = ['func1', 'func2', 'func3', 'func4']
    for f_name in func_names:
        eval(f_name)()
        print '-' * 20
