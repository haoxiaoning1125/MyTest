# coding=utf-8


class DataContainer(object):
    def __init__(self, uid, data):
        self.uid = uid
        self.data = data

    @property
    def get_uid(self):
        print 'get_id'
        return self.uid

    @property
    def get_data(self):
        print 'get_data'
        return self.data


if __name__ == '__main__':
    dc = DataContainer(1, 111)
    print dc.uid, dc.data
    print dc.get_uid, dc.get_data
