#!/usr/bin/env python3
'''begins of nqueen algo'''
from sys import argv


def usage_exit(msg):
    '''prints and exits'''
    print(msg)
    exit(1)


def _safe(b, rw, cl, N):
    '''checks safety'''
    for i in range(rw):
        if b[i] == cl or \
           b[i] - i == cl - rw or \
           b[i] + i == cl + rw:
            return False
    return True


def solve_nqueens(b, rw, N):
    '''works on nqueens'''
    if rw == N:
        print([[i, b[i]] for i in range(N)])
        return

    for cl in range(N):
        if _safe(b, rw, cl, N):
            b[rw] = cl
            solve_nqueens(b, rw + 1, N)
            b[rw] = -1


if __name__ == "__main__":
    if len(argv) != 2:
        usage_exit("Usage: nqueens N")

    try:
        N = int(argv[1])
    except ValueError:
        usage_exit("N must be a number")

    if N < 4:
        usage_exit("N must be at least 4")

    b = [-1] * N
    solve_nqueens(b, 0, N)
