#!/usr/bin/env python3
def pow(a, b):
    result = 1

    if b == 0:
        return 1

    if b < 0:
        b = -b
        for i in range(b):
            result *= a
        return 1 / result

    for i in range(b):
        result *= a

    return result
