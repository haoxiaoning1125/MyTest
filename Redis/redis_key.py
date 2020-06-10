# coding=utf-8
# redis键操作

import time
from redis import Redis

DIVIDING = '-' * 30


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    rc_keys = ['test_key1', 'test_key2', 'test', 'key']
    rc_values = [1, 2, 3, 4]
    for i in range(len(rc_keys)):
        rc.set(rc_keys[i], rc_values[i])
    print DIVIDING

    # exists: 判断一个键是否存在
    print rc.exists('tests')
    print rc.exists('test_key1')
    print DIVIDING

    # 判断键类型
    print rc.type('test_key1')
    print DIVIDING

    # 获取所有符合规则的键
    print rc.keys('*_*')
    print DIVIDING

    # 获取随机的一个键
    print rc.randomkey()
    print DIVIDING

    # 重命名键
    print rc.rename('test', 'test_rename')
    print rc.keys()
    print DIVIDING

    # 获取当前数据库中键的数目
    print rc.dbsize()
    print DIVIDING

    # 设定键的过期时间，单位为秒
    print rc.expire('test_rename', 1)

    # 获取键的过期时间，单位为秒，-1表示永久不过期, -2表示已过期
    print rc.ttl('test_rename')
    # time.sleep(1)
    # print rc.ttl('test_rename')
    # print rc.exists('test_rename')
    print DIVIDING

    # 删除键
    print rc.exists('key')
    print rc.delete('key')
    print rc.exists('key')
    print DIVIDING

    # 删除当前选择数据库中的所有键
    print rc.flushdb()

    # 删除所有数据库中的所有键
    print rc.flushall()

    rc.flushdb()
    rc.close()
