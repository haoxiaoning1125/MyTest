# coding=utf-8

import copy
from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        my_list = ['id: {}\n'.format(id(self))]
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            my_list.append('{}: {}'.format(i, ordered[i]))
            my_list.append('\n')
        return ''.join(my_list)


class ProtoType:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    book1 = Book('Fluent Python', 'Luciano Ramalho', 76.00)
    print book1

    prototype = ProtoType()
    prototype.register('book1', book1)
    book2 = prototype.clone('book1', price=89.00, pages=782)
    print book2
