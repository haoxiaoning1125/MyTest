# coding=utf-8


def first_have_n_digit(digit):
    """fib数列第一个拥有n位数字的是第几位"""
    a, b = 1, 1
    count = 0
    while len(str(a)) < digit:
        a, b = b, a + b
        count += 1
    return count


def fib_mod_prime(n, prime):
    """fib(10 ** 9) mod (10 ** 9 + 7)"""
    f0, f1 = 1, 1
    for i in range(n - 1):
        f0, f1 = f1 % prime, (f0 + f1) % prime
    return f1


if __name__ == '__main__':
    print first_have_n_digit(1000)
    print fib_mod_prime(10 ** 9, 10 ** 9 + 7)
