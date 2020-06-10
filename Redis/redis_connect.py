# coding=utf-8
# 创建redis连接

from redis import ConnectionPool, StrictRedis, Redis


if __name__ == '__main__':
    # rc = Redis(host='127.0.0.1', port=6379)  # 直接连接

    # pool = ConnectionPool(host='127.0.0.1', port=6379)  # 连接池
    # rc = StrictRedis(connection_pool=pool)

    pool = ConnectionPool.from_url('redis://127.0.0.1:6379')  # url
    rc = StrictRedis(connection_pool=pool)

    rc.flushdb()

    rc.set('hao', 123)
    print rc.get('hao')

    rc.flushdb()
    rc.close()
