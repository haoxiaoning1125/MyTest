# coding=utf-8

import random


class TreeType(object):
    apple_tree = 'apple_tree'
    cherry_tree = 'cherry_tree'
    peach_tree = 'peach_tree'


class Tree(object):
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if obj is None:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print 'type: {}, age: {}, at: ({}, {})'.format(self.tree_type, age, x, y)


if __name__ == '__main__':
    rnd = random.Random()
    age_min, age_max = 1, 30
    point_min, point_max = 0, 100
    tree_count = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(
            rnd.randint(age_min, age_max),
            rnd.randint(point_min, point_max),
            rnd.randint(point_min, point_max)
        )
        tree_count += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(
            rnd.randint(age_min, age_max),
            rnd.randint(point_min, point_max),
            rnd.randint(point_min, point_max)
        )
        tree_count += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(
            rnd.randint(age_min, age_max),
            rnd.randint(point_min, point_max),
            rnd.randint(point_min, point_max)
        )
        tree_count += 1

    print 'trees rendered: {}'.format(tree_count)
    print 'trees actually created: {}'.format(len(Tree.pool))

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print '{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5))
    print '{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6))
