# coding=utf-8
# is 比较地址, == 比较内容


if __name__ == '__main__':
    a = [1, 2]
    b = a
    print (a == b, a is b)
    b = a[:]
    print (a == b, a is b)
