#!/usr/bin/python3
'''this is utf-8 validation'''
from typing import List
import re


def validUTF8(data: List[int]) -> bool:
    '''function begins here'''
    bin_data = ['{0:08b}'.format(byte) for byte in data]
    str_bin = "".join(bin_data)
    _matching = re.compile(
        r'('
        r'0[01]{7}|'
        r'110[01]{5}10[01]{6}|'
        r'1110[01]{4}10[01]{6}10[01]{6}|'
        r'11110[01]{3}10[01]{6}10[01]{6}10[01]{6}'
        r')*'
    )
    res = _matching.fullmatch(str_bin)
    return res is not None