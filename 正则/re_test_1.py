# coding=utf-8

import re

if __name__ == '__main__':
    slist = ['l', 'li', 'lis', 'list']
    re_str = r'^[a-z]{2,4}$'
    for s in slist:
        if re.match(re_str, s):
            print (s, True)
        else:
            print (s, False)
