#!/usr/bin/python3

import math
# from decimal import *


def floatbin(n, precision=None, hwprint=False):
    """
    convert decimal to floating point binary form

    precision: <single|double> level of floating point precision to use
    hwprint: whether to print for homework output
    """
    if precision == 'single':
        bits = 23
        exponent = 2**8
    elif precision == 'double':
        bits = 52
        exponent = 2**11
    else:  # default
        bits = 100  # prevent overrun if calculation error
        exponent = 100
    limit = False
    # exponent
    while n < 0.5 and exponent > 0:
        n *= 2
        # n %= 1
        exponent -= 1
    # fraction
    binary = []
    print('{:>11}{:>11}   {}'.format('number', 'mult 2', 'binary'))
    while n != 1 and n != 0 and not limit:
        n *= 2
        binary.append(math.floor(n))
        if not hwprint:
            print('{:11.3f}{:11.3f}   {}'.format(n / 2, n, binstr(binary)))
        else:
            print('{:11.3f}{:11.3f}   {}'.format(n / 2, n, math.floor(n)))
        n %= 1
        if len(binary) > bits:
            limit = True
    return binstr(binary)


def binstr(lst):
    return ''.join([str(b) for b in lst])


if __name__ == '__main__':
    # floatbin(0.125)
    floatbin(625e-14, precision='double', hwprint=False)
