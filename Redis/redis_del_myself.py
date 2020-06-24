# coding=utf-8

from redis import Redis

DIVIDING = '-' * 50


def print_rc(rc):
    print 'keys : {}'.format(rc.keys())
    print 'index: {}'.format(rc.lrange('lt', 0, -1))
    print DIVIDING


if __name__ == '__main__':
    rc = Redis(host='127.0.0.1', port=6379)
    rc.flushdb()

    rc.lpush('lt', 'lt')
    rc.lpush('lt', 'key_1')
    rc.lpush('lt', 'key_2')
    rc.lpush('lt', 'key_3')
    rc.lpush('lt', 'key_4')

    rc.set('key_1', 1)
    rc.set('key_2', 2)
    rc.set('key_3', 3)
    rc.set('key_4', 4)

    print_rc(rc)

    to_del_keys = rc.lrange('lt', 0, -1)
    rc.delete(*to_del_keys)

    print_rc(rc)

    lt_exist = rc.exists('lt')
    print 'key \'lt\' {}exist'.format('' if lt_exist else 'not ')
