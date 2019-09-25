#coding=utf-8

if __name__ == '__main__':
    list = [11,22,33,44,55,66]
    list.sort(reverse=True)
    re=zip(range(1,5),list)
    re.sort(key=lambda x:x[1])
    print(re)