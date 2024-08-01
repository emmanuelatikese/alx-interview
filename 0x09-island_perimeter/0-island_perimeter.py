#!/usr/bin/python3
''' checking an algorithm
'''


def island_perimeter(grid):
    ''' checking for island
    '''
    p, con = 0, 0
    l_row, l_col = len(grid), len(grid[0])
    for x in range(l_row):
        for y in range(l_col):
            if grid[x][y] == 1:
                p += 4
                if x != 0 and grid[x - 1][y] == 1:
                    con += 1
                if y != 0 and grid[x][y - 1] == 1:
                    con += 1
    return p - 2 * con
