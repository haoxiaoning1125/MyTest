# coding=utf-8
# 最大公约数


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


if __name__ == '__main__':
    l1 = [69, 88, 86]
    l2 = [75, 256, 666]
    print [gcd(x, y) for x, y in zip(l1, l2)]
