#coding=utf-8

if __name__ == '__main__':
    f = lambda x,y,z:x+y+z
    print(f(1,2,3))

    L=[lambda x:x+2,lambda x:x*2,lambda x:x**2]
    for i in range(len(L)):
        print("L[%d]="%i,L[i](3))

    D={"1":lambda x:x*1,"2":lambda x:x*2,"3":lambda x:x**2}
    for i in range(1,len(D)+1):
        print("D[\"%d\"]="%i,D[str(i)](3))

    l = lambda: lambda x: x + 5
    b = l()
    print ("b=",b(2))               # b=7
    print ("==",(l())(2))           # ==7

    def inc(x):
        return x+10
    l=[1,2,3]
    print(map(inc,l))
    print(map(lambda x:x+10,l))