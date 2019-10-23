# coding=utf-8
# 线程同步队列 Queue(python2), queue(python3)

import Queue
import threading
import time


class MyThread2(threading.Thread):
    def __init__(self, thread_id, thread_name, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.queue = queue

    def run(self):
        print '{} started'.format(self.thread_name)
        process_data(self.thread_name, self.queue)
        print '{} exit'.format(self.thread_name)


exit_flag = 0
queue_lock = threading.Lock()
word_queue = Queue.Queue(10)


def process_data(name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not word_queue.empty():
            data = q.get()
            queue_lock.release()
            print '{} processing {}'.format(name, data)
        else:
            queue_lock.release()
        time.sleep(1)


thread_list = ['thread1', 'thread2', 'thread3']
name_list = ['one', 'two', 'three', 'four', 'five']
threads = []
thread_id = 1


if __name__ == '__main__':
    for tname in thread_list:
        thread = MyThread2(thread_id, tname, word_queue)
        thread.start()
        threads.append(thread)
        thread_id += 1

    queue_lock.acquire()
    for word in name_list:
        word_queue.put(word)
    queue_lock.release()

    while not word_queue.empty():
        pass

    exit_flag = 1

    for t in threads:
        t.join()
