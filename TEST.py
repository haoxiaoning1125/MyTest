if __name__ == '__main__':
    l = [1 for i in range(10)]
    for index, num in enumerate(l):
        if num == 1:
            l[index] = 10
    print l
