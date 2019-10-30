# coding=utf-8

import re


if __name__ == '__main__':
    # 忽略大小写
    clist = 'The fat cat sat on the mat.'.split(' ')
    print [c for c in clist if re.match('The', c)]
    print [c for c in clist if re.match('The', c, re.IGNORECASE)]

    # 贪婪匹配和惰性匹配
    str_ = 'The fat cat sat on the mat.'  # 'hhhat'
    res = re.compile('(.*at)')  # 贪婪匹配, 结果尽可能长
    print re.findall(res, str_)
    res = re.compile('(.*?at)')  # 惰性匹配, 结果尽可能短
    print re.findall(res, str_)

    # 单行模式和多行模式
    s = 'This is the first line.\nThis is the second line.\nThis is the third line.'
    q = re.match(r'This.*line.', s, flags=re.DOTALL)
    print q.group(0)

    # p = re.compile('.at')
    # print re.findall(p, s, re.MULTILINE)
