# coding=utf-8
# 双向列表, 高效实现插入和删除操作

from collections import deque

if __name__ == '__main__':
    # 固定长度, 队列满时, 最老的记录出队
    q = deque(maxlen=3)
    for i in range(4):
        q.append(i)
    print q

    q.pop()
    print q

    q.appendleft(10)
    print q
    q.popleft()
    print q

    q.extend([11, 12])
    print q

    q.extendleft([13, 14])
    print q
