# coding=utf-8

import json


if __name__ == '__main__':
    # json.dumps(): 将Python对象编码成json字符串
    data = [{
        'a': 1, 'b': 2, 'c': 3
    }]
    print json.dumps(data)
    print json.dumps(
        data,
        sort_keys=True,             # 按照key字典序排列
        indent=4,                   # 缩进
        separators=(',', ': ')      # 分隔符
    )
    print '-' * 20

    # json.loads(): 解码json数据, 返回Python字段的数据类型
    json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    print json.loads(json_data)
    print '-' * 20

    # json.dump(): 将Python对象编码成json并写入文件
    json_info = "{'age': 12}"
    f1 = open('write.json', 'w')
    json.dump(json_info, f1)

    # json.load(): 从文件解码json数据
