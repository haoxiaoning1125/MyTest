# coding=utf-8
# 命名元组

from collections import namedtuple

if __name__ == '__main__':
    Person = namedtuple('Person', ['name', 'age'])
    p = Person('hao', 22)
    print p
    print 'name:{}, age{}'.format(p.name, p.age)
    print 'type:{}'.format(type(p))
