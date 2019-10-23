# coding=utf-8
# 锁

import threading
from thread_test_2 import MyThread, print_name


class MyThread1(MyThread):
    def __init__(self, thread_id, thread_name, counter, thread_lock):
        MyThread.__init__(self, thread_id, thread_name, counter)
        self.thread_lock = thread_lock

    def run(self):
        print '{} start'.format(self.thread_name)
        self.thread_lock.acquire()
        print_name(self.thread_name, self.counter, 5)
        self.thread_lock.release()
        print '{} exit'.format(self.thread_name)


if __name__ == '__main__':
    thread_lock = threading.Lock()
    threads = []

    t1 = MyThread1(1, 'thread1', 0.3, thread_lock)
    t2 = MyThread1(2, 'thread2', 0.5, thread_lock)

    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
