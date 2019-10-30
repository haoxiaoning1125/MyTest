# coding=utf-8

import datetime


if __name__ == '__main__':
    a = datetime.datetime(2019, 7, 10)
    b = datetime.datetime(2019, 10, 1)
    print (b - a).days

    c = 59
    print (c / 10 + 1) * 10

    print '{0} {1} {0}'.format('a', 'b')
    print '{a} {b} {a}'.format(b='b', a='a')
