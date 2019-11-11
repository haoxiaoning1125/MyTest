import math


def bits_to_list(data):
    length=int(math.log(data,2))+1
    length=len(bin(data).replace('0b',''))
    length=40
    ret = []
    probe = 1 << (length - 1)
    for i in range(length):
        if probe & data != 0:
            ret.append(1)
        else:
            ret.append(0)
        probe >>= 1
    return ret


if __name__ == '__main__':
    print(bits_to_list(0b000101001))

    print(bin((1<<40)-1))
    print(len(bin((1<<40)-1).replace('0b','')))

    di={'1':1,'2':2}
    print('3' not in di)