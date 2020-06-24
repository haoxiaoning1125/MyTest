# coding=utf-8

from redis import Redis


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    print rc.lrange('a', 0, -1)

    rc.flushdb()
