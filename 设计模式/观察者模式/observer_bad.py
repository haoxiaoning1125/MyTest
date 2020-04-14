# coding=utf-8
# 员工上班在偷偷看股票，拜托前台一旦老板进来，就通知他们，让他们停止看股票。
# 两个类互相依赖, 高度耦合
# 问题出现:
# 增加看NBA, 打游戏等等等等摸鱼的员工
# python里鸭子类型的存在, 只要有update方法就可以被reception调用
# java里, 需要将各种摸鱼员工抽象为一个父类, reception调用父类的update方法


class Reception(object):  # 前台
    def __init__(self):
        self.observers = []

    def attach(self, observe):
        self.observers.append(observe)

    def notify(self):
        for observe in self.observers:
            observe.update()


class StockObserver(object):  # 看股票的摸鱼员工
    def __init__(self, name, reception):
        self.name = name
        self.reception = reception

    def update(self):
        print '{}, {} 停止看股票'.format(self.reception.status, self.name)


class NBAObserver(object):  # 看NBA的摸鱼员工
    def __init__(self, name, reception):
        self.name = name
        self.reception = reception

    def update(self):
        print '{}, {} 停止看NBA'.format(self.reception.status, self.name)


if __name__ == '__main__':
    reception = Reception()
    observer1 = StockObserver('张三', reception)
    observer2 = NBAObserver('李四', reception)
    reception.attach(observer1)
    reception.attach(observer2)
    reception.status = '老板来了'
    reception.notify()
