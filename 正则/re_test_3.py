# coding=utf-8
# 零宽断言
# 希望匹配一个字符串，这个字符串的前面或后面需要是特定的内容，但我们又不想要前面或后面的这个特定的内容

import re


if __name__ == '__main__':
    # 正预测先行断言: (?=exp)
    # 匹配一个位置之前的内容, 此位置满足正则exp
    s = "I'm singing while you're dancing."
    p = re.compile(r'\b\w+(?=ing\b)')
    print re.findall(p, s)

    # 正回顾后发断言: (?<=exp)
    # 匹配一个位置之后的文本, 此位置满足正则exp, 结果不包含此位置
    s = "doing done do todo"
    p = re.compile(r'(?<=\bdo)\w+\b')
    print re.findall(p, s)

    # 负预测先行断言: (?!exp)
    # 匹配一个位置之前的文本, 此位置不满足正则exp, 结果不包含此位置
    s = "done run going"  # ?
    p = re.compile(r'\b\w+(?!ing\b)')
    print re.findall(p, s)

    # 负回顾后发断言: (?<!exp)
    # 匹配一个位置之后的文本, 此位置不满足正则exp, 结果不包含此位置
    s = 'done run going'  # ?
    p = re.compile(r'(?<!\bdo)\w+\b')
    print re.findall(p, s)

    # 例子:
    # 匹配ip地址中的四个整数
    ip = '192.168.1.123'
    p = re.compile(r'(?<=\.)?\d+(?=\.)?')
    print re.findall(p, ip)

    # 匹配字符串s中的一些单词，这些单词不以’x’开头且不以’y’结尾：
    # ???
    s = 'xaay xbbc accd'
    p = re.compile(r'(?<!\bx)\w+(?!y\b)')
    print re.findall(p, s)

