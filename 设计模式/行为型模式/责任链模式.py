# coding=utf-8
# ATM
# 责任链, 保护代理, 懒惰初始化


class ATMModule:
    def __init__(self, num, next_one):
        self.num = num
        self.next_one = next_one

    def get(self, num_need):
        out = num_need / self.num
        if out != 0:
            print 'ATMMoudle {n1} out {n1} * {n2}'.format(n1=self.num, n2=out)
        if self.next_one:
            self.next_one.get(num_need - out * self.num)


class ATM:
    def __init__(self):
        self.module_first = None

    def get(self, num):
        if self.module_first is None:
            print 'init module......'
            module_1 = ATMModule(1, None)
            module_5 = ATMModule(5, module_1)
            module_10 = ATMModule(10, module_5)
            module_20 = ATMModule(20, module_10)
            module_50 = ATMModule(50, module_20)
            module_100 = ATMModule(100, module_50)
            self.module_first = module_100
        self.module_first.get(num)


if __name__ == '__main__':
    atm = ATM()
    while True:
        need = raw_input('how much need: ')
        if need.isdigit():
            atm.get(int(need))
        elif need == 'quit':
            break
        else:
            print 'unknown input'
