# coding=utf-8
#
# 有三个容积分别是3升、5升和8升的水桶，
# 其中容积为8升的水桶中装满了水，容积为3升和5升的水桶是空的。
# 都没有体积刻度，将8升水等分成两份，每份水都是4升水
#
# 状态搜索树

from collections import deque

INITIAL_BUCKET_STATE = [0, 0, 8]
BUCKET_VOLUME = [3, 5, 8]


def next_state_lawful(current_state, bucket_volume):
    next_action = [
        (_from, _to) for _from in range(3) for _to in range(3)
        if _from != _to and current_state[_from] > 0 and current_state[_to] < bucket_volume[_to]
    ]
    for _from, _to in next_action:
        next_state = list(current_state)
        if current_state[_from] + current_state[_to] > bucket_volume[_to]:
            next_state[_from] -= (bucket_volume[_to] - current_state[_to])
            next_state[_to] = bucket_volume[_to]
        else:
            next_state[_from] = 0
            next_state[_to] = current_state[_to] + current_state[_from]
        yield next_state


num = 0
record_list = []


def search_result(record, bucket_volume, final_bucket_state):
    global num, record_list
    current_state = record[-1]
    next_state = next_state_lawful(current_state, bucket_volume)

    for state in next_state:
        if state not in record:
            record.append(state)
            if state == final_bucket_state:
                print record
                record_list.append(deque(record))
                num += 1
            else:
                search_result(record, bucket_volume, final_bucket_state)
            record.pop()


if __name__ == '__main__':
    record = deque()
    record.append(INITIAL_BUCKET_STATE)
    search_result(record, [3, 5, 8], [0, 4, 4])
    print '-' * 20

    print 'result_num: {}'.format(num)
    print 'the shortest result: {}'.format(min(record_list, key=len))
