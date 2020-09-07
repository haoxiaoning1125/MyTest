# coding=utf-8
# pickle模块实现了用于序列化和反序列化Python对象结构的二进制协议

import pickle


if __name__ == '__main__':
    data = {
        'a': 110,
        'b': '111',
        'c': [112, 113, '114'],
        'd': {'d1': 115, 'd2': 116}
    }
    data_s = pickle.dumps(data)
    print data_s
    data_ = pickle.loads(data_s)
    print data_
