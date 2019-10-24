# coding=utf-8
# Event, Lock
# 两个Event不如信号量...

import time
import random
from threading import Thread, Event, Lock


class Boss(Thread):
    def __init__(self, id, product, events):
        Thread.__init__(self)
        self.id = id
        self.product = product
        self.events = events

    def run(self):
        for event in self.events:
            event.wait()
        print 'boss{}: {}'.format(self.id, self.product)


class Worker(Thread):
    def __init__(self, id, product, event, lock):
        Thread.__init__(self)
        self.id = id
        self.product = product
        self.event = event
        self.lock = lock

    def run(self):
        while True:
            self.lock.acquire()
            if len(self.product) < 10:
                time.sleep(random.random())
                add = random.randint(10, 100)
                self.product.append(add)
                self.lock.release()
                print 'worker {} add {}. product: {}'.format(self.id, add, self.product)
            else:
                self.lock.release()
                self.event.set()
                break


if __name__ == '__main__':
    event1 = Event()
    event2 = Event()
    lock = Lock()
    product = []
    ts = [
        Boss(1, product, [event1, event2]),
        Worker(1, product, event1, lock),
        Worker(2, product, event2, lock)
    ]
    for t in ts:
        t.start()
