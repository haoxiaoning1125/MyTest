# coding=utf-8
# bisect: bisect, insort
# 二分

import bisect


if __name__ == '__main__':
    data = range(0, 10, 2)
    print data

    bisect.insort(data, 7)
    print data

    print bisect.bisect(data, 7)
    print data

    print bisect.insort_left(data, 7)
    print data

    print bisect.insort_right(data, 7)
    print data

    print bisect.bisect_left(data, 7)
    print data

    print bisect.bisect_right(data, 7)
    print data
