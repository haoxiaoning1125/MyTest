# coding=utf-8


def mod_prime(x, y, p):
    """
    x ** y mod(p), p is a prime number.
    because:
        (x * y) mod p = ((x mod p) * (y mod p)) mod p
    """
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
            y = y - 1
        y = y >> 1
        x = (x * x) % p
    return res


if __name__ == '__main__':
    x, y, p = 2, 1000, 10 ** 9 + 7
    print mod_prime(x, y, p)
    print (x ** y) % p
