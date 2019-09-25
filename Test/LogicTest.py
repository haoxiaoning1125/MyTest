#coding=utf-8

"""
逻辑短路
"""

def f(num):
    print(num)
    return True if num%2==0 else False

if __name__ == '__main__':
    print(True or f(1))
    print(False and f(0))
    print(False or f(2))
    print(True and f(2))

