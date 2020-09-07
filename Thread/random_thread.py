# coding=utf-8
# random是否线程安全

import random
import threading
import time

s = threading.Semaphore(0)


def random_num(thread_id, seed):
    print 'thread_id: {}, set seed: {}'.format(thread_id, seed)
    if s.acquire():
        random.seed(seed)
        # time.sleep(10)
        print 'thread_id: {}, gen random num: {}'.format(thread_id, random.randint(1, 100))


if __name__ == '__main__':
    t1 = threading.Thread(target=random_num, args=(1, 1))
    t2 = threading.Thread(target=random_num, args=(2, 2))

    t1.start()
    # time.sleep(5)
    t2.start()

    with s._Semaphore__cond:
        s._Semaphore__value += 2
        s._Semaphore__cond.notifyAll()

    t1.join()
    t2.join()