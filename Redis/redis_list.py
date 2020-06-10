# coding=utf-8
# redis列表操作

from redis import Redis
from redis.exceptions import ResponseError

DIVIDING = '-' * 30


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    # 在列表末尾添加元素
    print rc.rpush('list', 4, 5, 6)

    # 在列表头添加元素
    print rc.lpush('list', 3, 2, 1)

    # 返回列表指定下标间的元素
    print rc.lrange('list', 0, -1)
    print DIVIDING

    # 列表长度
    print rc.llen('list')
    print DIVIDING

    # 返回指定下标的元素
    print rc.lindex('list', 2)
    print rc.lrange('list', 0, -1)
    print DIVIDING

    # 给列表中指定下标赋值, 越界则报错
    print rc.lset('list', 0, 100)
    try:
        print rc.lset('list', 100, 100)
    except ResponseError as re:
        print re
    print rc.lrange('list', 0, -1)
    print DIVIDING

    # 删除count个键的列表中值为value的元素
    print rc.rpush('list_rem', 1, 1, 1, 2, 2, 2)
    print rc.lrange('list_rem', 0, -1)
    print rc.lrem('list_rem', count=2, value=2)
    print rc.lrange('list_rem', 0, -1)
    print DIVIDING

    # 弹出列表首元素并删除
    print rc.lrange('list', 0, -1)
    print rc.lpop('list')

    # 弹出列表尾元素并删除
    print rc.rpop('list')
    print rc.lrange('list', 0, -1)
    print DIVIDING

    # 截取列表指定下标之间的元素, 并保留在原列表中
    print rc.ltrim('list', 2, 4)
    print rc.lrange('list', 0, -1)

    rc.flushdb()
    rc.close()
