# coding=utf-8
# 线程类

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print '{} start'.format(self.thread_name)
        print_name(self.thread_name, self.counter, 5)
        print '{} exit'.format(self.thread_name)


def print_name(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print '{}: {}'.format(thread_name, time.ctime(time.time()))
        counter -= 1


if __name__ == '__main__':
    thread1 = MyThread(1, 'thread1', 0.5)
    thread2 = MyThread(2, 'thread2', 0.5)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()