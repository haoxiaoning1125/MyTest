# coding=utf-8

if __name__ == '__main__':
    num = raw_input('input a number: ')
    num = int(num)
    print num
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        print num
        if num == 1:
            break
