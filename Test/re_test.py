# coding=utf-8

import re


if __name__ == '__main__':
    re_s = '^[0-9a-zA-Z].*\.py'
    ss = [
        '__init__.py', 'LogicTest.py', 're_test.py', '2.py',
        're_test_py',
        '__init__.log', 'LogicTest.log', 're_test.log'
    ]
    for s in ss:
        print s if re.match(re_s, s) else None
