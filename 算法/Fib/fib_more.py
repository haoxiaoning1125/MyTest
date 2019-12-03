# coding=utf-8
from Decorator.decorator import time_of_


def first_have_n_digit(n):
    """
    the index of the first num in fib which has n digits
    """
    a, b = 0, 1
    count = 0
    while len(str(a)) < n:
        a, b = b, a + b
        count += 1
    return count


@time_of_
def fib_mod_prime(n, p):
    """
    F(n) mod p = (F(n-1) + F(n-2)) mod p = (F(n-1) mod p + F(n-2) mod p) mod p
    """
    f0, f1 = 0, 1
    for i in xrange(n):
        f0, f1 = f1, (f0 + f1) % p
        # print f0
    return f0


if __name__ == '__main__':
    print first_have_n_digit(1000)
    print fib_mod_prime(10 ** 9, 10 ** 9 + 7)
    print fib_mod_prime(20, 100)
