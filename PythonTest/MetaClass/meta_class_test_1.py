# coding=utf-8
# 元类
# https://www.liaoxuefeng.com/wiki/897692888725344/923030550637312
# 通过type()函数创建类


def func(self, name='world'):
    print 'Hello {}'.format(name)


if __name__ == '__main__':
    # 参数: 类名, 父类(支持多继承), 方法名绑定函数
    Hello = type('Hello', (object,), dict(hello=func))
    hello = Hello()
    hello.hello()
    hello.hello('233')
