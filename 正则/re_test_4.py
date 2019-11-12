# coding=utf-8

import re


if __name__ == '__main__':
    string = '\python'
    ret = re.search('\\\\python', string)
    print ret.group()
    ret = re.search(r'\\python', string)
    print ret.group()
