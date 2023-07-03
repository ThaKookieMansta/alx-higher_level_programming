#!/usr/bin/python3
"""
This module nqueens is a backtracking program to print coordinates of n queens
"""

from sys import argv


def existing_queen(y):
    """
    Checks whether a queen exists
    :param y:
    :return:
    """
    for x in range(n):
        if y == a[x][1]:
            return True
    return False


def discard(x, y):
    """
    This function determines if the coordinates will be used or
    discarded
    :param x:
    :param y:
    :return:
    """
    if existing_queen(y):
        return False
    q = 0
    while q < x:
        if abs(a[q][1] - y) == abs(q - x):
            return False
        q += 1
    return True


def discard_ans(x):
    """
    Discards the answers from failure
    :param x:
    :return:
    """
    for ans in range(x, n):
        a[ans][1] = None


def nqueens(x):
    """
    This function will use backtracking to find
    the solution
    :param x:
    :return:
    """
    for y in range(n):
        discard_ans(x)
        if discard(x, y):
            a[x][1] = y
            if x == n - 1:
                print(a)
            else:
                nqueens(x + 1)


if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(n):
        a.append([i, None])

    nqueens(0)
