#!/usr/bin/python3
'''finding the min operation'''


def minOperations(n):
    '''the algorithm starts here'''
    div, min_op = 2, 0
    while n > 1:
        if n % div == 0:
            n = n / div
            min_op += div
        else:
            div += 1
    return min_op
