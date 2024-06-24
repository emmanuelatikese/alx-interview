#!/usr/bin/python3
'''here is where all the stat goes'''
import sys


stat_count = {x: 0 for x in ['200', '301', '400', '401',
                             '403', '404', '405', '500']}
file_size = 0
count= 0

try:
    for line in sys.stdin:
        ln = line.split(' ')
        if len(ln) > 2:
            stat_code = ln[-2]
            c_stat = ln[-1]
        if stat_code in stat_count:
            stat_count[stat_code] += 1
        file_size += int(c_stat)
        count += 1
        if count == 10:
            print('File size: {:d}'.format(file_size))
            sort_key = sorted(stat_count.keys())
            for key in sort_key:
                if stat_count[key] != 0:
                    print('{}: {}'.format(key, stat_count[key]))
            count = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(file_size))
    sort_key = sorted(stat_count.keys())
    for key in sort_key:
        if stat_count[key] != 0:
            print('{}: {}'.format(key, stat_count[key]))
