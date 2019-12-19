# coding=utf-8

import demjson


if __name__ == '__main__':
    data = [{
        'a': 1, 'b': 2, 'c': 3
    }]
    json_data = demjson.encode(data)
    print json_data

    data_ = demjson.decode(json_data)
    print data_

    print data == data_
