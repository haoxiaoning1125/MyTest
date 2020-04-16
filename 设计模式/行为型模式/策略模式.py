# coding=utf-8
# 定义了一系列封装的算法, 使它们可以互相替换
# 算法的变化不影响算法的客户
# 例: 商场活动: 正常收费, 打折收费, 返利收费


class CashSuper(object):
    # 收费算法抽象类
    def accept_money(self, money):
        pass


class NormalCash(CashSuper):
    # 正常收费算法类
    def accept_money(self, money):
        return money


class DiscountCash(CashSuper):
    # 打折收费算法类
    def __init__(self, discount=1.0):
        self.discount = discount

    def accept_money(self, money):
        return money * self.discount


class ReturnCash(CashSuper):
    # 返利收费算法类
    def __init__(self, money_condition=0.0, money_return=0.0):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_money(self, money):
        if money >= self.money_condition:
            return money - (money / self.money_condition) * self.money_return
        else:
            return money


class Context(object):
    # 具体策略类
    def __init__(self, c_super):
        self.c_super = c_super

    def get_result(self, money):
        return self.c_super.accept_money(money)


if __name__ == '__main__':
    contexts = [
        Context(NormalCash()),
        Context(DiscountCash(0.8)),
        Context(ReturnCash(100.0, 10.0)),
    ]
    money = 100.0
    for context in contexts:
        print context.get_result(money)
