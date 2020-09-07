# coding=utf-8

from redis import Redis


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    star = 1300
    lefttime = 86400 * 100
    rc.zadd('z', {1083557: star * 10 ** 7 + lefttime})
    # rc.zadd('z', 1083999, 100)
    print rc.zrange('z', 0, -1, withscores=True)
    print help(redisranker.client.zadd)
    rc.flushdb()
