# coding=utf-8
# 最小栈


class MinStack():
    def __init__(self):
        self._stack = []
        self._min = -1
        self._length = 0

    def push(self, num):
        if not self._stack:
            self._min = num
            self._stack.append(0)
        else:
            compare = num - self._min
            self._stack.append(compare)
            self._min = num if compare < 0 else self._min
        self._length += 1

    def pop(self):
        top = self._stack.pop()
        self._min = (self._min - top) if top < 0 else self._min
        return self._min + top
    
    def get_min(self):
        return self._min

    def get_stack(self):
        return self._stack

    def get_length(self):
        return self._length


if __name__ == '__main__':
    min_stack = MinStack()
    add_list = [10, 9, 12, 1, -100, 300]
    for num in add_list:
        min_stack.push(num)
        print 'push: {}, min: {}, stack: {}'.format(num, min_stack.get_min(), min_stack.get_stack())

    print '-' * 40

    for i in range(min_stack.get_length()):
        num = min_stack.pop()
        print 'pop: {}, min: {}, stack: {}'.format(num, min_stack.get_min(), min_stack.get_stack())
