# coding=utf-8


class Controller(object):
    _singleton = None

    def __new__(cls, *args, **kwargs):
        print '__new__ has be called.'
        if not cls._singleton:
            print 'create ton.'
            # print super(Controller, cls)
            cls._singleton = super(Controller, cls).__new__(cls, *args, **kwargs)
            return cls._singleton

    @staticmethod
    def echo(s):
        """静态方法, 不对类属性进行操作"""
        print s


if __name__ == '__main__':
    c1 = Controller()
    if c1:
        c1.echo('c1')
    print '-' * 20

    c2 = Controller()
    if c2:
        c2.echo('c2')
    print '-' * 20

    c3 = Controller._singleton
    if c3:
        c3.echo('c3')
        print c1 is c3
