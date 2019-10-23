# coding=utf-8
# 线程函数

import threading
import time


def target(thread_id, thread_name):
    print '{}, {}'.format(thread_id, thread_name)
    time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=target, args=(1, 'thread1'))
    t2 = threading.Thread(target=target, args=(2, 'thread2'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
