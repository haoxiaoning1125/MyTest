# coding=utf-8


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'a synthesizer named {}'.format(self.name)

    @staticmethod
    def play():
        return 'synthesizer.play'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'this is {}'.format(self.name)

    @staticmethod
    def speak():
        return 'human.speak'


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'a computer named {}'.format(self.name)

    @staticmethod
    def execute():
        return 'computer.execute'


class Adapter:
    """适配器类"""
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.update_dict(**adapted_methods)

    def __str__(self):
        return str(self.obj)

    def update_dict(self, **adapted_methods):
        self.__dict__.update(adapted_methods)


if __name__ == '__main__':
    objects = [Computer('MacBook')]
    syn = Synthesizer('moog')
    objects.append(Adapter(syn, execute=syn.play))
    human = Human('Bob')
    objects.append(Adapter(human, execute=human.speak))

    for ob in objects:
        print ob.execute()  # 通过适配器调用目标类中与execute对应的方法
    print '-' * 20

    # 当所有类都有一个属性name时, 以下代码会运行失败
    for ob in objects:
        try:
            print ob.name  # 适配器没有提供对name属性的访问
        except AttributeError as ae:
            print ae
    print '-' * 20

    # 在适配器中添加对name属性的访问后, 报错消失
    objects[1].update_dict(name=syn.name)
    objects[2].update_dict(name=human.name)

    for ob in objects:
        print ob.name
