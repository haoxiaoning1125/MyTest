# coding=utf-8


class Publisher:
    def __init__(self, name, data):
        self.observers = []
        self.name = name
        self.data = data

    def __str__(self):
        return '{} has data {}'.format(self.name, self.data)

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print 'failed to append {}'.format(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print 'failed to remove {}'.format(observer)

    def notify(self):
        for o in self.observers:
            o.notify(self.name, self.data)


class HexFormatter:
    def __init__(self, name):
        self.name = name

    def notify(self, publisher_name, data):
        print '{}: {} has now hex data {}'.\
            format(self.name, publisher_name, hex(data))


class BinaryFormatter:
    def __init__(self, name):
        self.name = name

    def notify(self, publisher_name, data):
        print '{}: {} has now bin data {}'.\
            format(self.name, publisher_name, bin(data))


if __name__ == '__main__':
    publisher = Publisher('publisher', 100)
    print publisher
    print '-' * 20

    hf = HexFormatter('hex_formatter')
    bf = BinaryFormatter('binary_formatter')
    publisher.add(hf)
    publisher.add(bf)
    publisher.notify()
    print '-' * 20

    publisher.remove(hf)
    publisher.notify()

