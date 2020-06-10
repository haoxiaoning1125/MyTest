# coding=utf-8
# redis字符串操作

from redis import Redis

DIVIDING = '-' * 30


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    # 给数据库中键为name的string赋予值value
    print rc.set('s', 111)

    # 返回数据库中键为name的string的value
    print rc.get('s')
    print type(rc.get('s'))
    print DIVIDING

    # 给数据库中键为name的string赋予值value并返回上次的value
    print rc.getset('s', 222)
    print rc.get('s')
    print DIVIDING

    # 如果不存在这个键值对，则更新value，否则不变
    print rc.setnx('s', 0)
    print rc.setnx('snx', 0)
    print rc.get('s')
    print rc.get('snx')
    print DIVIDING

    # 为多个键设置value
    mapping = dict(s1='vs1', s2='vs2')
    print rc.mset(mapping)

    # 返回多个键对应的value
    print rc.mget('s1', 's2')
    print DIVIDING

    # 键均不存在时才批量赋值
    mapping = dict(uxs1='vs1', uxs2='vs2')
    print rc.msetnx(mapping)
    print rc.mget('uxs1', 'uxs2')
    print DIVIDING

    # 键为name的value增值操作，默认为1，键不存在则被创建并设为amount
    rc.set('num', 1)
    print rc.incr('num', amount=2)
    print rc.incrby('num', amount=3)

    # 键为name的value减值操作，默认为1，键不存在则被创建并设为-amount
    print rc.decr('num', amount=3)
    print rc.decrby('num', amount=3)
    print DIVIDING

    # 键为name的string的值追加value
    rc.set('append', 'asd')
    print rc.append('append', 'asdasdasd')
    print rc.get('append')
    print DIVIDING

    # 返回键为name的string的子串
    print rc.substr('append', 0, 5)

    # 获取键的value值从start到end的子字符串
    print rc.getrange('append', 0, 5)

    rc.flushdb()
    rc.close()
