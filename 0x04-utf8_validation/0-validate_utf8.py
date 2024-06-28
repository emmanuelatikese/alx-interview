#!/usr/bin/env python3
'''this is utf-8 validation'''


def validUTF8(data):
    '''function begins here'''
    n = len(data)
    i = 0

    while i < n:
        _byt = data[i]
        if _byt >> 7 == 0:
            nbytes = 1
        elif _byt >> 5 == 0b110:
            nbytes = 2
        elif _byt >> 4 == 0b1110:
            nbytes = 3
        elif _byt >> 3 == 0b11110:
            nbytes = 4
        else:
            return False
        if i + nbytes > n:
            return False
        for x in range(1, nbytes):
            if data[i + x] >> 6 != 0b10:
                return False
        i = i + nbytes
        return True
