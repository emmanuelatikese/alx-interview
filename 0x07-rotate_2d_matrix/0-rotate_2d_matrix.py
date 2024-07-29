#!/usr/bin/python3
'''File contains 2d rotation func
'''


def rotate_2d_matrix(matrix):
    '''function to rotate
    '''
    mat_len = len(matrix)
    for x in range(mat_len):
        for j in range(x, mat_len):
            matrix[x][j], matrix[j][x] = matrix[j][x], matrix[x][j]
    for i in range(mat_len):
        matrix[i].reverse()
