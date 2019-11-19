# coding=utf-8
# timeit

import timeit

CODE_1 = """
for i in range(REPEAT_TIMES):
    a.append(func())
"""

CODE_2 = """
a = [func() for i in range(REPEAT_TIMES)]
"""

SETUP = """
a = []
REPEAT_TIMES = 10000

def func():
    return 1
"""


if __name__ == '__main__':
    times = (100, 1000)
    for num in times:
        print 'num = {}'.format(num)
        print timeit.timeit(stmt=CODE_1, setup=SETUP, number=num)
        print timeit.timeit(stmt=CODE_2, setup=SETUP, number=num)

    print '-' * 20

    for num in times:
        print 'num = {}'.format(num)
        print timeit.repeat(stmt=CODE_1, setup=SETUP, number=num, repeat=2)
        print timeit.repeat(stmt=CODE_2, setup=SETUP, number=num, repeat=2)
