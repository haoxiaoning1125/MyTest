# coding=utf-8


class T:
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == '__main__':
    t1 = T(1, 2)
    t2 = T(None, None)
    print hasattr(t1, 'a')
    print hasattr(t1, 'b')
    print hasattr(t1, 'c')
    print hasattr(t2, 'a')
    print hasattr(t2, 'b')
    print hasattr(t2, 'c')
