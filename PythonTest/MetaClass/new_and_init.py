# coding=utf-8
# 新类和旧类
# http://www.360doc.com/content/17/1229/19/10849989_717476226.shtml


class A(object):
    """
    新类, 创建时先调用__new__产生对象, 再调用__init__初始化
    __new__函数不返回, 则不会调用__init__
    """
    def __init__(self):
        print 'init {}'.format(self.__class__)

    def __new__(cls, *args, **kwargs):
        print 'new {}'.format(cls)
        return object.__new__(cls, *args, **kwargs)


class B:
    """
    旧类, 调用__init__创建对象并初始化, 不调用__new__
    """
    def __init__(self):
        print 'init {}'.format(self.__class__)

    def __new__(cls, *args, **kwargs):
        print 'new {}'.format(cls)
        return object.__new__(cls, *args, **kwargs)


class C(object):
    def __new__(cls, *args, **kwargs):
        ret_class = type('Add', (object,), dict(add=lambda self, x, y: x + y))
        return ret_class()


if __name__ == '__main__':
    a = A()
    b = B()
    print '-' * 20

    c = C()
    print type(c)
    print c.add(1, 2)

