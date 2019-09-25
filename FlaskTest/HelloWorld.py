class A:
    name=1

def setname(cla,name):
    cla.name=name

if __name__ == '__main__':
    a=A()
    setname(a,2)
    print(a.name)

    a=(1,2,3)
    print(a[2])