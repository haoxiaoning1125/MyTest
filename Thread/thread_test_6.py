# coding=utf-8
# 生产者消费者, 锁

import time
import threading
import random


class Producer(threading.Thread):
    def __init__(self, name, queue, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.lock = lock

    def run(self):
        while True:
            self.lock.acquire()
            if len(self.queue) < 5:
                pro = random.randint(10, 100)
                self.queue.append(pro)
                time.sleep(0.5)
                self.lock.release()
                print '{} produce {}, queue: {}'.format(self.name, pro, self.queue)
            else:
                self.lock.release()


class Consumer(threading.Thread):
    def __init__(self, name, queue, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.lock = lock

    def run(self):
        while True:
            self.lock.acquire()
            if not len(self.queue) == 0:
                con = self.queue.pop(0)
                time.sleep(1)
                self.lock.release()
                print '{} consume {}, queue: {}'.format(self.name, con, self.queue)
            else:
                self.lock.release()


if __name__ == '__main__':
    queue = []
    lock = threading.Lock()

    pros = [Producer('p1', queue, lock), Producer('p2', queue, lock), Producer('p3', queue, lock)]
    cons = [Consumer('c1', queue, lock), Consumer('c2', queue, lock)]

    for p in pros:
        p.start()

    for c in cons:
        c.start()
