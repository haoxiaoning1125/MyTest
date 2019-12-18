import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        print("call...")
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    print super(SingletonType, cls)
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo():
    __metaclass__ = SingletonType

    def __init__(self, name):
        self.name = name
        print("init Foo", self.name)

    def __repr__(self,):
        return "{}:{}\n".format(self.name, id(self))


if __name__ == '__main__':
    obj1 = Foo('name1')
    obj2 = Foo('name2')
    print(obj1, obj2)
