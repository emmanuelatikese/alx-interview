#!/usr/bin/python3
'''begins of nqueen algo'''
from sys import argv


def nqueen(n):
    '''this is where the algo starts'''
    col= set()
    posdiag = set()
    negdiag = set()
    res = []
    positions = []

    def backtracking(r):
        '''this is does the backtracking'''
        if r == n:
            res.append(positions[:])
            return
        for c in range(n):
            if c in col or (r + c) in posdiag or (r - c) in negdiag:
                continue
            col.add(c)
            posdiag.add(r + c)
            negdiag.add(r - c)
            positions.append([r, c])
            backtracking(r + 1)
            col.remove(c)
            posdiag.remove(r + c)
            negdiag.remove(r - c)
            positions.pop()

    backtracking(0)
    return res


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
        solutions = nqueen(n)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be an number")
        exit(1)
