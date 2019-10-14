# coding=utf-8
# a说我不是小偷；
# b说c是小偷；
# c说小偷肯定是d；
# d说c胡说！
# 其中有三个人说的是实话，一个人说的是假话，请编程推断谁是小偷（用穷举法和逻辑表达式）


def thief_is():
    for thief in ['a', 'b', 'c', 'd']:
        sum = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief != 'd')
        if sum == 3:
            print 'thief is {}'.format(thief)
            break


if __name__ == '__main__':
    thief_is()
