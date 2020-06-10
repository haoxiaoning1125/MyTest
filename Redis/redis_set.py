# coding=utf-8
# redis集合

from redis import Redis

DIVIDING = '-' * 30


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    # 添加元素
    print rc.sadd('s', 1, 2, 3, 4, 5)
    print rc.sadd('s', 1, 6)
    print rc.smembers('s')
    print DIVIDING

    # 删除元素
    print rc.srem('s', 1)
    print rc.srem('s', 100)
    print rc.smembers('s')
    print DIVIDING

    # 元素个数
    print rc.scard('s')
    print DIVIDING

    # 是否是集合中的元素
    print rc.sismember('s', 100)
    print rc.sismember('s', 2)
    print DIVIDING

    rc.sadd('s1', 1, 2, 3)
    rc.sadd('s2', 2, 3, 4)
    print 's1: {}'.format(rc.smembers('s1'))
    print 's2: {}'.format(rc.smembers('s2'))
    # 差集
    print 's1 - s2: {}'.format(rc.sdiff('s1', 's2'))
    # 交集
    print 's1 ^ s2: {}'.format(rc.sinter('s1', 's2'))
    # 并集
    print 's1 | s2: {}'.format(rc.sunion('s1', 's2'))
    print DIVIDING

    # 返回所有元素
    print rc.smembers('s')

    # 随机返回并删除一个元素
    print rc.spop('s')
    print rc.smembers('s')

    # 随机返回一个元素但不删除
    print rc.srandmember('s')
    print rc.smembers('s')

    rc.flushdb()
    rc.close()
