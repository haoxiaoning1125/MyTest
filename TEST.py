if __name__ == '__main__':
    l = [1, 2]
    print l
    print id(l)
    l *= 2
    print l
    print id(l)

    t = (1, 2)
    print t
    print id(t)
    t *= 2
    print t
    print id(t)