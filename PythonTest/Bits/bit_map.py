# coding=utf-8


def get_bits_num(data, shift, width):
    return (data >> shift) & ((1 << width) - 1)


def set_bits_num(data, shift, width, new):
    if new >= 1 << width:
        new = (1 << width) - 1
    return (data & (~(((1 << width) - 1) << shift))) | (new << shift)


def add_bits_num(data, shift, width, add):
    old = get_bits_num(data, shift, width)
    new = min((1 << width) - 1, old + add)
    return set_bits_num(data, shift, width, new)
