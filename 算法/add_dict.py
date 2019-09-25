# coding=utf-8
# a = {'a': 1, 'b': 2}
# b = {'a': 2}
# a + b = {'a': 3, 'b': 2}


def add_dict_1(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1.keys():
            dict1[k] += v
        else:
            dict1[k] = v
    return dict1


def add_dict_2(dict1, dict2):
    ret = dict(dict1)
    for k, v in dict2.items():
        if k in ret.keys():
            ret[k] += v
        else:
            ret[k] = v
    return ret


if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 2}

    # print add_dict_1(dict1, dict2)
    # print dict1
    # print dict2

    print add_dict_2(dict1, dict2)
    print dict1
    print dict2
