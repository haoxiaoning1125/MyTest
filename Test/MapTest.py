#coding=utf-8

if __name__ == '__main__':
    l=[1,2,3,4,5]
    l=map(lambda x:x**2,l)
    print(l)

    for index,value in enumerate(l,start=1):
        print("index:%s,value:%s"%(index,value))

    l=list(enumerate(l,start=1))
    print(l)