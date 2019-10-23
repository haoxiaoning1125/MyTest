# coding=utf-8
# 锁服务于共享资源
# 信号量服务于多个线程的执行顺序

import threading


a, b, c = 0, 0, 0
sema = threading.BoundedSemaphore(2)


def get_a():
    global a
    a = 1
    sema.acquire()


def get_b():
    global b
    b = 2
    sema.acquire()


def get_c():
    sema.release()
    sema.release()
    global c
    c = a + b


if __name__ == '__main__':
    ts = [
        threading.Thread(target=get_a),
        threading.Thread(target=get_b),
        threading.Thread(target=get_c)
    ]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print a, b, c
