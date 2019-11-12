# coding=utf-8

import re


if __name__ == '__main__':
    clist = ['-1', '1', '1211', '-1211', 'a', 'A', '-', '']
    print [c for c in clist if re.match('^-?[0-9]+$', c)]
    print [c for c in clist if re.match('^-?[0-9]*$', c)]
    print [c for c in clist if re.match('^-?[^0-9]+$', c)]

    clist = ['a.', 'aa', 'ab']
    print [c for c in clist if re.match('^a\.$', c)]
    print [c for c in clist if re.match('^a[.]$', c)]
    print [c for c in clist if re.match('^a.$', c)]

    clist = ['1.1', '1.11', '1.111', '1.1111', '1.11111', '11.11', '111.11']
    print [c for c in clist if re.match('^[0-9]+[.][0-9]{2,4}$', c)]
    print [c for c in clist if re.match('^[0-9]+[.][0-9]{2,}$', c)]

    clist = 'The car is parked in the garage.'.split(' ')
    print [c for c in clist if re.match('(c|g|p)ar', c)]
    print [c for c in clist if re.match('(c|g|p)ar|i[a-z]', c)]

    clist = 'The fat cat sat on the mat.'.split(' ')
    print [c for c in clist if re.match('(f|c|m)at\.', c)]

    # \  |  转义
    # .  |  除换行符外的所有字符
    # [] |  匹配[]中列举的字符
    # \w |  匹配所有单词字符, 等同于[a-zA-Z0-9_]
    # \W |  匹配所有非单词字符, 等同于[^\w]
    # \d |  匹配数字, [0-9]
    # \D |  匹配非数字, [^\d]
    # \s |  匹配所有空白字符, 等同于[\t\n\f\r\p{Z}]
    # \S |  匹配所有非空白字符, [^\s]
    # \f |  匹配一个换页符
    # \n |  匹配一个换行符
    # \r |  匹配一个回车符
    # \t |  匹配一个制表符
    # \v |  匹配一个垂直制表符
    # \b |  单词边界, 字与空格间的位置
    # \B |  非单词边界

    # re.match(r_str, str): 从头匹配
    # re.findall(r_str, str): 找出所有符合条件的字符串并返回列表
    # re.search(r_str, str): 不从头匹配, 匹配成功返回一个值
    # re.sub(r_str, s_new, s_old): 将匹配到的部分替换
    # re.split(r_str, str): 切割并返回一个列表
