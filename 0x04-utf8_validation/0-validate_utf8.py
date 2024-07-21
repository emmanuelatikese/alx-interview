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
        if j == 0:
            i += 1
        elif j == 1 or j > 4:
            return False
        else:
            k = i + j
            if k > len(data):
                return False
            for x in range(i + 1, k):
                if checking(data[x]) != 1:
                    return False
            i = k
    return True
