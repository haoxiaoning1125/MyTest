# coding=utf-8
# x % (2 ** n) <==> x & (2 ** n - 1)


if __name__ == '__main__':
    for n in range(10):
        for x in range(10):
            print x % (2 ** n) == x & (2 ** n - 1)
