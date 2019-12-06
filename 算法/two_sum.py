# coding=utf-8
# 给定一个整数数组nums和一个目标值target, 请你在该数组中找出和为目标值的那两个整数, 并返回他们的数组下标(由小到大)


def two_sum_1(nums, target):
    """数组有序"""
    m = 0
    n = len(nums) - 1
    while m < n:
        sum_ = nums[m] + nums[n]
        if sum_ < target:
            m += 1
        elif sum_ > target:
            n -= 1
        else:
            return [m, n]
    return [-1, -1]


def two_sum_2(nums, target):
    """数组无序"""
    dic = dict()
    for i, num in enumerate(nums):
        if target - num in dic:
            j = dic[target - num]
            return [i, j] if i < j else [j, i]
        else:
            dic[num] = i
    return [-1, -1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15, 19]
    print two_sum_1(nums, 21)
    nums = [19, 7, 11, 2, 15]
    print two_sum_2(nums, 34)
