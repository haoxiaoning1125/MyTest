# coding=utf-8

import time
import threading
import Queue


class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                break
            foo = self.queue.get()
            time.sleep(0.5)
            print '{} process {}'.format(self.name, str(foo))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue.Queue(20)
    for i in range(20):
        queue.put(i)
    for i in range(10):
        threadname = 'thread_' + str(i)
        w = Worker(threadname, queue)
        w.start()
    queue.join()
