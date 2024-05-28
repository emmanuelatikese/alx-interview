#!/usr/bin/python3
'''this is all about pascal algo'''


def pascal_triangle(n):
    """This is initials of the algorithm"""
    if n <= 0:
        return []
    list_ans = []
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(list_ans[i - 1][j] + list_ans[i - 1][j - 1])
        list_ans.append(tmp)
    return list_ans
