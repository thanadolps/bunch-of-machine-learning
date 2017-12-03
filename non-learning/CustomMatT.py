from typing import Callable
from numpy import diag

def diag_mat(deg : int, func : Callable[[int],int]  = lambda x : x) :
    A = diag([(func(deg)) / 2] * (deg), 0)

    for i in range(1, deg):
        A += diag([func(deg - i)] * (deg - i), i)

    A += A.T

    return A

if __name__ == '__main__':
    pass

