# coding=utf-8
# 信号量

import time
import threading

MAX_THREAD_NUM = 5
semlock = threading.BoundedSemaphore(MAX_THREAD_NUM)


def show_fun(n):
    print '{} started, {}'.format(n, time.ctime())
    time.sleep(5)
    print '{} ended, {}'.format(n, time.ctime())
    semlock.release()


if __name__ == '__main__':
    # 使用信号量控制线程个数
    list = []
    for i in range(8):
        semlock.acquire()
        t = threading.Thread(target=show_fun, args=(i,))
        list.append(t)
        t.start()
