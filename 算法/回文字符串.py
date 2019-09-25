# coding=utf-8


def is_palindromic(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    s_list = ['abcccba', 'acccda', '', 'a', 'ab']
    print [is_palindromic(s) for s in s_list]
