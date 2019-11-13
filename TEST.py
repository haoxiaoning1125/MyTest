def func(a, b=2, c=1):
    pass


if __name__ == '__main__':
    print func.__defaults__
    print func.__code__.co_varnames
