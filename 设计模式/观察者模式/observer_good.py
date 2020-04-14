# coding=utf-8
# 解决: 将耦合部分抽象为一个父类, 方便后期维护

from abc import ABCMeta, abstractmethod


class Subject():  # 事件
    __metaclass__ = ABCMeta
    observers = []
    status = ''

    @abstractmethod
    def attach(self, observer):  # 添加观察者
        pass

    @abstractmethod
    def detach(self, observer):  # 移除观察者
        pass

    @abstractmethod
    def notify(self):  # 通知观察者
        pass


class Observer():  # 观察者
    __metaclass__ = ABCMeta

    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    @abstractmethod
    def update(self):  # 更新状态
        pass


class Boss(Subject):
    def __init__(self):
        pass

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class StockObserver(Observer):
    def update(self):
        print '{}, {}停止看股票'.format(self.sub.status, self.name)


class NBAObserver(Observer):
    def update(self):
        print '{}, {}停止看NBA'.format(self.sub.status, self.name)


if __name__ == '__main__':
    boss = Boss()
    observer1 = StockObserver('张三', boss)
    observer2 = NBAObserver('李四', boss)
    boss.attach(observer1)
    boss.attach(observer2)
    boss.status = '老板来了'
    # boss.detach(observer1)
    boss.notify()
