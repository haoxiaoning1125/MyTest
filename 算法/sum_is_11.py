# coding=utf-8


def sum_is_1(list_, count):
    start = 0
    end = len(list_) - 1
    while start < end:
        sum = list_[start] + list_[end]
        if sum < count:
            start += 1
        elif sum > count:
            end -= 1
        else:
            print '{}+{}={}'.format(list_[start], list_[end], count)
            break
    else:
        print 'not found'


def sum_is_2(list_, count):
    dic = dict()
    for i in range(len(list_)):
        m = list_[i]
        if count - m in dic:
            print '{}+{}={}'.format(count - m, m, count)
            break
        dic[m] = count - m
    else:
        print 'not found'


if __name__ == '__main__':
    list_ = [3, 4, 5, 7, 10]
    count = 18
    sum_is_1(list_, count)
    sum_is_2(list_, count)
