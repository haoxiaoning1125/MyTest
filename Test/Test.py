def func(**kwargs):
    for item in kwargs.items():
        print item


if __name__ == '__main__':
    k1 = ['a', 'b', 'c']
    v1 = [1, 2, 3]
    k2 = ['d', 'e', 'f']
    v2 = [4, 5, 6]
    dic1 = dict(zip(k1, v1))
    dic2 = dict(zip(k2, v2))
    func(**dict(dic1.items() + dic2.items()))
