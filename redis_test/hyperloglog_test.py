# coding=utf-8
# HyperLogLog, 伯努利过程
# 占用空间小, 但牺牲部分精确性

import redis


if __name__ == '__main__':
    client = redis.StrictRedis()
    for i in range(1000):
        client.pfadd('codehole', 'user%d' % i)
        total = client.pfcount('codehole')
        if total != i + 1:
            print total, i + 1
            break
