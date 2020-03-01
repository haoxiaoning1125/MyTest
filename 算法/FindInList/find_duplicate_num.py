# coding=utf-8
# 已知一个数组nums存在n+1个整数, 每个整数 1 <= num <= n,
# 证明数组中存在重复数字并找出
# 例:
#   nums = [1, 1, 2, 3, 4]
#   return 1


def find_duplicate_num_1(nums):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                return nums[i]
    return -1


def find_duplicate_num_2(nums):
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return -1


def find_duplicate_num_3(nums):
    s = set()
    for num in nums:
        if num not in s:
            s.add(num)
        else:
            return num
    return -1


def find_duplicate_num_4(nums):
    """快慢指针, 将数组元素作为下标, 若存在重复, 必有至少两个下标指向数组同一位置"""
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return nums.index(slow)


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 4, 6]
    print find_duplicate_num_1(nums)
    print find_duplicate_num_2(nums)
    print find_duplicate_num_3(nums)
    print find_duplicate_num_4(nums)
