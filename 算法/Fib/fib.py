# coding=utf-8
# 1, 1, 2, 3, 5.....


def fib_1(n):
    if n < 2:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    fib = [1, 1]
    for i in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


def fib_3(n):
    f0, f1 = 1, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


if __name__ == '__main__':
    NUM = 10 ** 9
    # print fib_1(NUM)
    # print fib_2(NUM)
    print fib_3(NUM)
