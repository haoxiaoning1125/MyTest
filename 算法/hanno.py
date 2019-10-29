# coding=utf-8


def hanno(n, a='A', b='B', c='C'):
    def _hanno(n, a, b, c):
        global count
        if n == 1:
            count += 1
            print '{} -> {}'.format(a, c)
        else:
            _hanno(n - 1, a, c, b)
            count += 1
            print '{} -> {}'.format(a, c)
            _hanno(n - 1, b, a, c)

    global count
    count = 0
    _hanno(n, a, b, c)
    print count


if __name__ == '__main__':
    n = 3
    hanno(n)
