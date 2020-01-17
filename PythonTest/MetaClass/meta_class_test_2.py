# coding=utf-8
# 通过metaclass创建类
# metaclass适用于需要动态地通过输入参数创建类的场景

# class定义了如何产生object, 其本身也是object, 可赋值给其他变量、拷贝、作为参数
# type()是python用来创建所有class的metaclass, (type是自身的metaclass)
# a = 10; a.__class__; a.__class__.__class__; a.__class__.__class__.__class__


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        """
        :param cls: 当前准备创建的类的对象
        :param name: 类名
        :param bases: 类继承的父类集合
        :param attrs: 类的方法集合
        """
        attrs['add'] = lambda self, value: self.append(value)
        attrs['pop_'] = lambda self: self.pop()
        print name
        print bases
        print attrs
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass  # 指示解释器通过ListMetaclass.__new__()创建MyList


if __name__ == '__main__':
    my_list = MyList()
    for i in range(10):
        my_list.add(i)
    print my_list
    print my_list.pop_()
    print my_list
