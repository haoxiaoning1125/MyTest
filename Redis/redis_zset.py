# coding=utf-8
# redis有序集合

from redis import Redis

DIVIDING = '-' * 30


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    # 添加元素
    print rc.zadd('z', {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500})
    print rc.zrevrange('z', 0, -1, withscores=True)

    # 删除元素
    print rc.zrem('z', 'a')
    print rc.zrevrange('z', 0, -1, withscores=True)
    print DIVIDING

    # 元素已存在, 增加分值, 元素不存在, 添加元素
    print rc.zincrby('z', 50, 'b')
    print rc.zincrby('z', 100, 'a')
    print rc.zrevrange('z', 0, -1, withscores=True)
    print DIVIDING

    # 返回元素的排名, 从小到大, 元素不存在返回None
    members = ['a', 'b', 'c', 'd', 'e']
    print ['{}: {}'.format(member, rc.zrank('z', member)) for member in members]
    print 'f: {}'.format(rc.zrank('z', 'f'))

    # 返回元素的排名, 从大到小, 元素不存在返回None
    members = ['a', 'b', 'c', 'd', 'e']
    print ['{}: {}'.format(member, rc.zrevrank('z', member)) for member in members]
    print 'f: {}'.format(rc.zrank('z', 'f'))
    print DIVIDING

    # 返回分值在给定区间内的元素
    print rc.zrangebyscore('z', 200, 400, withscores=True)

    # 返回分值在给定区间内的元素数量
    print rc.zcount('z', 200, 400)

    # 返回有序集合元素个数
    print rc.zcard('z')
    print DIVIDING

    # 删除排名在给定区间内的元素
    print rc.zadd('z1', {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500})
    print rc.zrange('z1', 0, -1, withscores=True)
    print rc.zremrangebyrank('z1', 0, 2)
    print rc.zrange('z1', 0, -1, withscores=True)
    print DIVIDING

    # 删除分值在给定区间内的元素
    print rc.zadd('z2', {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500})
    print rc.zrange('z2', 0, -1, withscores=True)
    print rc.zremrangebyscore('z2', 200, 400)
    print rc.zrange('z2', 0, -1, withscores=True)

    rc.flushdb()
    rc.close()
