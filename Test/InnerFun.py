#coding=utf-8

"""
嵌套函数
"""

def outer():
    def inner():
        print("inner.")

    inner()
    print("outer.")

if __name__ == '__main__':
    outer()
    # inner()
    # outer().inner()