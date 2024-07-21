#!/usr/bin/python3
'''this is utf-8 validation function file'''


def validUTF8(data):
    '''function validUTF8 begins here which does validation'''
    def checking(num):
        '''comparing num to bytes
        '''
        mask = 1 << 7
        count = 0
        while num & mask:
            mask >>= 1
            count += 1
        return count
    i = 0
    while i < len(data):
        j = checking(data[i])
        k = i + j + (j != 0)
        i += 1
        if j == 1 or j > 4 or k > len(data):
            return False
        while i < len(data) and i <= k:
            cur = checking(data[i])
            if cur != 1:
                return False
            i += 1
        return True
