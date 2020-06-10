# coding=utf-8
# redis散列表

from redis import Redis

DIVIDING = '-' * 30


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    # 添加映射
    print rc.hset('h', 'a', 0)
    print rc.hgetall('h')

    # 批量添加映射
    print rc.hmset('h', {'a': 1, 'b': 2, 'c': 3, 'd': 4})
    print rc.hgetall('h')
    print DIVIDING

    # 获取所有键
    print rc.hkeys('h')

    # 获取所有值
    print rc.hvals('h')

    # 获取所有键值对
    print rc.hgetall('h')
    print DIVIDING

    # 如果键不存在, 则添加键值对
    print rc.hsetnx('h', 'a', 2)
    print rc.hsetnx('h', 'e', 5)
    print rc.hgetall('h')
    print DIVIDING

    # 返回多个键对应的值
    print rc.hmget('h', 'a', 'b')

    # 设置多个键对应的值
    print rc.hmset('h', {'a': 11, 'b': 22})
    print rc.hgetall('h')
    print DIVIDING

    # 将键对应的值增长amount
    print rc.hincrby('h', 'a', 11)
    print rc.hincrbyfloat('h', 'b', 0.1)
    print rc.hgetall('h')
    print DIVIDING

    # 是否存在键
    print rc.hexists('h', 'a')

    # 键值对个数
    print rc.hlen('h')

    rc.flushdb()
    rc.close()
