# coding=utf-8
# 观察者模式:
# 定义对象间的一对多依赖关系, 当一个对象的状态发生变化时, 所有依赖于它的对象得到通知并做出相应操作
# 又称: 发布/订阅, 消息通知机制, 事件监听, 事件驱动编程
# 例: 生成订单的同时发送短信和微信


class Order(object):
    def __init__(self, id):
        self.id = id
        self.observers = []

    def append_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def modify(self):
        for observer in self.observers:
            observer.update(self.id)


class Observer(object):
    def update(self, order_id):
        pass


class OrderObserver(Observer):
    def update(self, order_id):
        print '订单{}, 处理数据.'.format(order_id)


class MessageObserver(Observer):
    def update(self, order_id):
        print '订单{}, 发送短信.'.format(order_id)


class WeChatObserver(Observer):
    def update(self, order_id):
        print '订单{}, 发送微信.'.format(order_id)


if __name__ == '__main__':
    new_order1 = Order(1)
    order_observer = OrderObserver()
    message_observer = MessageObserver()
    wechat_observer = WeChatObserver()

    new_order1.append_observer(order_observer)
    new_order1.append_observer(message_observer)
    new_order1.append_observer(wechat_observer)

    new_order1.modify()
