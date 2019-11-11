#coding=utf-8

"""
用n & (n-1)消除最后的一位1
"""

import random


def judge(num):
    # 判断2的整数幂
    return num & (num-1) == 0


def one_count(num):
    # 2进制中1的个数
    count=0
    while num!=0:
        count+=1
        num=num&(num-1)
    return count


def bit_change_count(a,b):
    # 把数a转成数b，需要改变多少二进制位
    return one_count(a^b)


if __name__ == '__main__':
    # for i in range(1,20):
    #     # print(i,bin(i),judge(i))
    #     print(i,bin(i),one_count(i))
    for i in range(10):
        a=random.randint(1,100)
        b=random.randint(1,100)
        print(a,bin(a),b,bin(b),bit_change_count(a,b))
