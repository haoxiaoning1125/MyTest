# coding=utf-8
# 1, 1, 2, 3, 5.....


def fib_1(n):
    if n < 2:
        return n
    else:
        return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    fib = [0, 1]
    for i in xrange(n):
        fib.append(fib[-1] + fib[-2])
    return fib[-2]


def fib_3(n):
    f0, f1 = 0, 1
    for i in xrange(n):
        f0, f1 = f1, f0 + f1
    return f0


if __name__ == '__main__':
    # for NUM in range(10):
    #     print [fib_1(NUM), fib_2(NUM), fib_3(NUM)]
    print len(str(fib_3(4781)))
    print len(str(fib_3(4782)))
